currency	fbentity	product	
USD	U	ADS	Y
USD	I	ADS	Y
USD	U	CREDIT	Y
USD	I	CREDIT	Y
non USD	U	ADS	N
non USD	I	ADS	Y
non USD	U	CREDIT	N
non USD	I	CREDIT	N




load data local infile '/tmp/chcheung/payout_report' into table payout_report;

fe_mapping = {}
for row in payout_ids:
  key_tuple = tuple(str(row[key]) for key in backfill_keys)
  if key_tuple not in fe_mapping:
    fe_mapping[key_tuple] = {'financial_id': 0, 'time_created': 0}
  if (not fe_mapping[key_tuple]['financial_id']):
    fe_mapping[key_tuple]['financial_id'] = row['financial_id']
    fe_mapping[key_tuple]['time_created'] = row['time_created']

account_detail_file = temputil.mktemp()
output = []
for row in account_details:
  row = dict(zip(extract_keys, row))
  if not int(row['financial_id']):
    key_tuple = tuple(str(row[key]) for key in backfill_keys)
    row['financial_id'] = fe_mapping.get(key_tuple, 0)
  output.append(tuple(str(row[key]) for key in extract_keys))
generate_payout_file(account_detail_file, output)
return account_detail_file



# @lint-avoid-python-3-compatibility-imports
from collections import deque
import sys

# List of all report module names.
ALL_REPORTS = ["AdsFundingReport",
               "AdsPaymentReport",
               "AdsReport",
               "AltPayReport",
               "AltPayRefundReport",
               "App2UserReport",
               "AppCreditTrackingReport",
               "ApplicationReport",
               "ConvertBalanceReport",
               "ExpireCreditsReport",
               "FundingSourceReport",
               "GiftcardPEReport",
               "GiftcardReport",
               "InstrumentReport",
               "OutstandingBalanceDeltaReport",
               "PdbReport",
               "PSReport",
               "ReceivingReport",
               "SubscriptionReport",
               "UserWalletReport"]

# List of all report sections that use OrderDB
ORDERDB_REPORTS = ["GiftcardRedemption",
                   "GiftcardRedemptionExternal",
                   "SubscriptionSale",
                   "SubscriptionRefund",
                   "SubscriptionChargeback",
                   "A2UXNewChargeback",
                   "A2UXSale",
                   "A2USale"]

DEPENDENCE_CONFIG = {
  "AdsPaymentReport": ["ApplicationReport.AppChargeback"],
  "ApplicationReport": ["AltPayReport"],
  "PSReport.PSPayment": ["AppCreditTrackingReport.RecvAppCreditTracking"]
}

ALL_REPORTS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
DEPENDENCE_CONFIG = {
  "1": ["6.1"],
  "2": ["6.2"],
  "3": ["8.1", "7"],
  "4": ["8.2"],
  "6": ["11"],
  "6.1": ["7"],
  "6.2": ["7"],
  "8.1": ["9.1"],
  "8.2": ["10"]
}
REP_SEC = {
  "root": ["root"],
  "1": ["1.1"],
  "2": ["2.1"],
  "3": ["3.1"],
  "4"59273011.82: ["4.1"],
  "5": ["5.1"],
  "6": ["6.1", "6.2", "6.3"],
  "7": ["7.1"],
  "8": ["8.1", "8.2"],
  "9": ["9.1", "9.2"],
  "10": ["10.1"],
  "11": ["11.1"]
}

_FULL_NAME_TO_MODULE = {}
_SHORT_NAME_TO_MODULE = {}
_SHORT_NAME_MAPPING = {}
REPORT_SECTION = {'root': ['root']}

for report, sub_reports in REP_SEC.iteritems():
  REPORT_SECTION[report] = sub_reports

#for report_name in ALL_REPORTS:
#  _FULL_NAME_TO_MODULE[report_name] = __import__(report_name,
#                                                 globals(), locals(), [], -1)
#  REPORT_SECTION[report_name] = (
#    ['.'.join([report_name, section]) for section in
#     _FULL_NAME_TO_MODULE[report_name].ALL_REPORT_SECTIONS])

#for report_name, report_module in _FULL_NAME_TO_MODULE.iteritems():
#  _SHORT_NAME_TO_MODULE[report_module.REPORT_SHORT_NAME] = report_module
#  _SHORT_NAME_MAPPING[report_module.REPORT_SHORT_NAME] = report_name

def get_report_module(module_name):
  """Returns a report module given the report's full name."""
  return _FULL_NAME_TO_MODULE.get(module_name)

def get_report_module_by_short_name(short_name):
  """Returns a report module given the report's short 3-letter name."""
  return _SHORT_NAME_TO_MODULE.get(short_name)

def get_all_modules():
  return _FULL_NAME_TO_MODULE.values()

def _convert_to_full_name(report):
  if report == 'root':
    return report
  report_split = report.split('.')
  if report_split[0] in _FULL_NAME_TO_MODULE:
    pass
  elif report_split[0].upper() in _SHORT_NAME_TO_MODULE:
    report_split[0] = _SHORT_NAME_MAPPING[report_split[0].upper()]
  else:
    print >> sys.stderr, "No such report: %s" % report
  return '.'.join(report_split)

def _get_sub_reports(reports):
  if isinstance(reports, str):
    reports = [reports]
  sub_reports = []
  for report in reports:
    #report = _convert_to_full_name(report)
    report_split = report.split('.')
    if len(report_split) == 1:
      sub_reports.extend(REPORT_SECTION[report])
    else:
      sub_reports.append(report)
  return sub_reports

def _append_into_config(config, reports, sub_reports):
  for report in reports:
    config[report]['sub_reports'].extend(sub_reports)
  for sub_report in sub_reports:
    config[sub_report]['parents_reports'].extend(reports)

def _parse_config(config):
  parsed = {}
  for report, sub_reports in REPORT_SECTION.iteritems():
    for sub_report in sub_reports:
      parsed[sub_report] = {'parents_reports': [], 'sub_reports': []}
  config['root'] = ALL_REPORTS
  for report, sub_reports in config.iteritems():
    reports = _get_sub_reports(report)
    sub_reports = _get_sub_reports(sub_reports)
    _append_into_config(parsed, reports, sub_reports)
  return parsed

def _init_dependents_search(reports):
  config = _parse_config(DEPENDENCE_CONFIG)
  req_reports = set([])
  for report in reports:
    #report = _convert_to_full_name(report)
    if report in REPORT_SECTION:
      req_reports |= set(REPORT_SECTION[report])
    elif report in config:
      req_reports.add(report)
    else:
      print >> sys.stderr, "No such report: %s" % report
  return (config, req_reports)

def _topo_sorting(reports, config):
  que = deque(['root'])
  counter = {report: 0 for report in reports}
  sorted_reports = []
  while que:
    cur = que.pop()
    for report_name in config[cur]['sub_reports']:
      if report_name not in reports:
        continue
      counter[report_name] += 1
      assert report_name in config
      if counter[report_name] == len(config[report_name]['parents_reports']):
        que.append(report_name)
        sorted_reports.append(report_name)

  if 'root' in reports:
    reports.remove('root')
  assert len(sorted_reports) == len(reports)
  return sorted_reports

def get_corelate_reports(reports, config, field):
  que = deque(reports)
  while que:
    cur = que.pop()
    report_list = config[cur][field]
    if field == 'sub_reports':
      report_list = _get_sub_reports(
        set([report.split('.')[0] for report in report_list]))
    for report_name in report_list:
      if report_name not in reports:
        reports.add(report_name)
        que.append(report_name)

def get_interdependence_reports(reports):
  config, req_reports = _init_dependents_search(reports)
  get_corelate_reports(req_reports, config, 'sub_reports')
  get_corelate_reports(req_reports, config, 'parents_reports')
  return _topo_sorting(req_reports, config)

def get_backfill_reports(reports):
  config, req_reports = _init_dependents_search(reports)
  get_corelate_reports(req_reports, config, 'sub_reports')
  return set([report.split('.')[0] for report in req_reports])
