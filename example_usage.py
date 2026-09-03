from client import CompetitorMapPriceViolationMonitorClient

def main():
    client = CompetitorMapPriceViolationMonitorClient()
    res = client.inspect_map_compliance()
    print('MAP Price Monitor: ' + res['monitoring_run_id'] + ' (Violations: ' + str(res['violations_detected']) + ')')
    print('Action: ' + res['action_recommended'])
    print('Evidence URL: ' + res['evidence_screenshot_url'])

if __name__ == '__main__':
    main()
