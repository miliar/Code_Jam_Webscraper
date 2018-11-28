#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	unsigned int tc_count;
	cin >> tc_count;
	for (unsigned tc = 0;tc<tc_count;tc++) {
		vector<vector<char > > data;
		unsigned int row, column;
		cin >> row >> column;
		for (unsigned int r = 0;r<row;r++) {
			string temp;
			cin >> temp;
			vector<char> data_entr;
			for (unsigned int c = 0;c<column;c++) {
				data_entr.push_back(temp.at(c));
			}
			data.push_back(data_entr);
		}
		vector <vector< string > > scan_d;
		for (unsigned int c = 0;c < column;c++) {
			vector <string> scan_entr;
			for (unsigned int r = 0;r < row;r++) {
				if (data[r][c] == '?') { continue; }
				else {
					string temp = "";
					temp.append(1, data[r][c]);
					scan_entr.push_back(temp);
					scan_entr.push_back(to_string(r));
				}
			}
			if (scan_entr.size() == 0) {
				scan_entr.push_back("NONE");
			}
			scan_d.push_back(scan_entr);
		}
			unsigned int start_c;
			for (start_c = 0;start_c<column;start_c++) {
				if (scan_d[start_c].size() == 1) { continue; }
				else { break; }
			}
			unsigned int presv = start_c;
			vector <char> prev_config;
			for (start_c = start_c;start_c<column;start_c++) {
				if (scan_d[start_c].size() == 2) {
					char temp = scan_d[start_c][0].at(0);
					prev_config.clear();
					for (unsigned int r = 0;r<row;r++) {
						data[r][start_c] = temp;
						prev_config.push_back(temp);
					}
				}
				else if (scan_d[start_c].size() == 1) {
					for (unsigned int r = 0;r<row;r++) {
						data[r][start_c] = prev_config[r];
					}
				}
				else {
					prev_config.clear();
					for (unsigned int el = 0;el * 2<scan_d[start_c].size();el++) {
						unsigned int until = stoi(scan_d[start_c][(el * 2) + 1], NULL, 10);
						char temp = scan_d[start_c][el * 2].at(0);
						if ((el * 2) + 2>=scan_d[start_c].size()) {
							while (prev_config.size()<row) {
								prev_config.push_back(temp);
							}
						}
						else {
							while (prev_config.size()<until+1) {
								prev_config.push_back(temp);
							}
						}
					}
					for (unsigned int r = 0;r<row;r++) {
						data[r][start_c] = prev_config[r];
					}
				}
			}
			if (presv != 0) {
				vector<char> cp_start;
				for (unsigned int r = 0;r<row;r++) {
					cp_start.push_back(data[r][presv]);
				}
				for (signed int temp = presv;temp>-1;temp--) {
					for (unsigned int r = 0;r<row;r++) {
						data[r][temp] = cp_start[r];
					}
				}
			}
			cout << "Case #" << tc + 1 << ":" << '\n';
			for (unsigned int r = 0;r<row;r++) {
				for (unsigned int c = 0;c<column;c++) {
					cout << data[r][c];
				}
				cout << '\n';
			}
		}
	return 0;
}
