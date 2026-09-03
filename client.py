class CompetitorMapPriceViolationMonitorClient:
    def inspect_map_compliance(self, brand_sku='SKU_SPEAKER_PRO', authorized_map_usd=199.00, detected_competitor_offers=None):
        if detected_competitor_offers is None:
            detected_competitor_offers = [
                {'reseller': 'Discount Electronics Inc', 'advertised_price': 169.00, 'in_stock': True},
                {'reseller': 'Prime Retailer', 'advertised_price': 199.00, 'in_stock': True}
            ]
        violations = [o for o in detected_competitor_offers if o['advertised_price'] < authorized_map_usd]
        return {
            'monitoring_run_id': 'map_mon_7721',
            'brand_sku': brand_sku,
            'authorized_map_usd': authorized_map_usd,
            'violations_detected': len(violations),
            'infringing_resellers': [v['reseller'] for v in violations],
            'action_recommended': 'ISSUE_FORMAL_MAP_CEASE_AND_DESIST_NOTICE',
            'evidence_screenshot_url': 'https://prisync.pricing.genpark.ai/violations/7721.json'
        }
