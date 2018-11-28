#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
using namespace std;

bool isnumberincreasing(unsigned long long n);
void numberofnumbers(string n);

int main()
{
	/*
	ifstream myIn;
	myIn.open("C:\\Users\\Simeon\\Downloads\\largetest2.in");
	ofstream MyOut;
	MyOut.open("C:\\Users\\Simeon\\Desktop\\LETSFKENGOMATE.txt");
	*/
	int cases = 0;
	cin >> cases;
	
	for (int i = 0; i < cases; i++) {
		string s = "";
		cin >> s;

	
		cout << "Case #" << i + 1 << ": ";
		numberofnumbers(s);
			cout << endl;
	}
	return 0;
}

void numberofnumbers(string n) {


	string k = n;
	string ss = n;
	unsigned long long k2 = stoull(k);
	bool check = false;
	sort(ss.begin(), ss.end());
	vector<int> YAH(n.length());
	vector<int> YAH2(n.length());
	vector<int> vf(n.length());
	for (int i = 0; i < n.length(); i++) {
		char a = k[i];
		int t = a - 48;
		YAH[i] = t;
		YAH2[i] = t;
		vf[i] = t;
	}

	sort(YAH2.begin(), YAH2.end());

	if (k2 < 10 || k == ss)
		cout << k2;
	
	else if (YAH[0] == YAH2[n.length() - 1] || YAH[1] < YAH[0]) {
		if (YAH[0] == 1) {
			for (int i = 0; i < n.length() - 1; i++) {
				cout << "9";
			}
		}
		else {
			cout << YAH[0] - 1;
			for (int i = 0; i < n.length() - 1; i++) {
				cout << "9";
			}
		}
	} // close second else if largest and if 1 or not
	else {

		

			for (int i = 0; i < n.length() - 1; i++) {
				if (YAH[i + 1] >= YAH[i])
					vf[i] = YAH[i];
				else
				{
					vf[i] = (YAH[i] - 1);
					for (int o = i + 1; o < n.length(); o++) {
						vf[o] = 9;
					}
					break;
				}
			}
			
			for (int h = 0; h < n.length() - 1; h++) {
				if (vf[h + 1] >= vf[h])
					vf[h] = vf[h];
				else
				{
					vf[h] = (vf[h] - 1);
					for (int o = h + 1; o < n.length(); o++) {
						vf[o] = 9;
					}
					break;
				}
			}

			for (int h = 0; h < n.length() - 1; h++) {
				if (vf[h + 1] >= vf[h])
					vf[h] = vf[h];
				else
				{
					vf[h] = (vf[h] - 1);
					for (int o = h + 1; o < n.length(); o++) {
						vf[o] = 9;
					}
					break;
				}
			}

			for (int h = 0; h < n.length() - 1; h++) {
				if (vf[h + 1] >= vf[h])
					vf[h] = vf[h];
				else
				{
					vf[h] = (vf[h] - 1);
					for (int o = h + 1; o < n.length(); o++) {
						vf[o] = 9;
					}
					break;
				}
			}

			for (int h = 0; h < n.length() - 1; h++) {
				if (vf[h + 1] >= vf[h])
					vf[h] = vf[h];
				else
				{
					vf[h] = (vf[h] - 1);
					for (int o = h + 1; o < n.length(); o++) {
						vf[o] = 9;
					}
					break;
				}
			}

			for (int h = 0; h < n.length() - 1; h++) {
				if (vf[h + 1] >= vf[h])
					vf[h] = vf[h];
				else
				{
					vf[h] = (vf[h] - 1);
					for (int o = h + 1; o < n.length(); o++) {
						vf[o] = 9;
					}
					break;
				}
			}

			for (int h = 0; h < n.length() - 1; h++) {
				if (vf[h + 1] >= vf[h])
					vf[h] = vf[h];
				else
				{
					vf[h] = (vf[h] - 1);
					for (int o = h + 1; o < n.length(); o++) {
						vf[o] = 9;
					}
					break;
				}
			}

			for (int h = 0; h < n.length() - 1; h++) {
				if (vf[h + 1] >= vf[h])
					vf[h] = vf[h];
				else
				{
					vf[h] = (vf[h] - 1);
					for (int o = h + 1; o < n.length(); o++) {
						vf[o] = 9;
					}
					break;
				}
			}

			for (int h = 0; h < n.length() - 1; h++) {
				if (vf[h + 1] >= vf[h])
					vf[h] = vf[h];
				else
				{
					vf[h] = (vf[h] - 1);
					for (int o = h + 1; o < n.length(); o++) {
						vf[o] = 9;
					}
					break;
				}
			}

			for (int h = 0; h < n.length() - 1; h++) {
				if (vf[h + 1] >= vf[h])
					vf[h] = vf[h];
				else
				{
					vf[h] = (vf[h] - 1);
					for (int o = h + 1; o < n.length(); o++) {
						vf[o] = 9;
					}
					break;
				}
			}

			for (int h = 0; h < n.length() - 1; h++) {
				if (vf[h + 1] >= vf[h])
					vf[h] = vf[h];
				else
				{
					vf[h] = (vf[h] - 1);
					for (int o = h + 1; o < n.length(); o++) {
						vf[o] = 9;
					}
					break;
				}
			}

			for (int h = 0; h < n.length() - 1; h++) {
				if (vf[h + 1] >= vf[h])
					vf[h] = vf[h];
				else
				{
					vf[h] = (vf[h] - 1);
					for (int o = h + 1; o < n.length(); o++) {
						vf[o] = 9;
					}
					break;
				}
			}

			for (int h = 0; h < n.length() - 1; h++) {
				if (vf[h + 1] >= vf[h])
					vf[h] = vf[h];
				else
				{
					vf[h] = (vf[h] - 1);
					for (int o = h + 1; o < n.length(); o++) {
						vf[o] = 9;
					}
					break;
				}
			}

			for (int h = 0; h < n.length() - 1; h++) {
				if (vf[h + 1] >= vf[h])
					vf[h] = vf[h];
				else
				{
					vf[h] = (vf[h] - 1);
					for (int o = h + 1; o < n.length(); o++) {
						vf[o] = 9;
					}
					break;
				}
			}

			for (int h = 0; h < n.length() - 1; h++) {
				if (vf[h + 1] >= vf[h])
					vf[h] = vf[h];
				else
				{
					vf[h] = (vf[h] - 1);
					for (int o = h + 1; o < n.length(); o++) {
						vf[o] = 9;
					}
					break;
				}
			}

			for (int h = 0; h < n.length() - 1; h++) {
				if (vf[h + 1] >= vf[h])
					vf[h] = vf[h];
				else
				{
					vf[h] = (vf[h] - 1);
					for (int o = h + 1; o < n.length(); o++) {
						vf[o] = 9;
					}
					break;
				}
			}

			for (int h = 0; h < n.length() - 1; h++) {
				if (vf[h + 1] >= vf[h])
					vf[h] = vf[h];
				else
				{
					vf[h] = (vf[h] - 1);
					for (int o = h + 1; o < n.length(); o++) {
						vf[o] = 9;
					}
					break;
				}
			}

			for (int h = 0; h < n.length() - 1; h++) {
				if (vf[h + 1] >= vf[h])
					vf[h] = vf[h];
				else
				{
					vf[h] = (vf[h] - 1);
					for (int o = h + 1; o < n.length(); o++) {
						vf[o] = 9;
					}
					break;
				}
			}
			for (int h = 0; h < n.length() - 1; h++) {
				if (vf[h + 1] >= vf[h])
					vf[h] = vf[h];
				else
				{
					vf[h] = (vf[h] - 1);
					for (int o = h + 1; o < n.length(); o++) {
						vf[o] = 9;
					}
					break;
				}
			}
		

		if(vf[0] != 0) {
		for (int i = 0; i < n.length(); i++)
			cout << vf[i];
		}
		else
		{
			for (int i = 1; i < n.length(); i++)
				cout << vf[i];
		}
	}
}