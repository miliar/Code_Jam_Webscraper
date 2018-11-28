#include<iostream>
#include<vector>
#include<iomanip>
using namespace std;

int main() {
	int num = 0;
	double dist = 0.0;
	int dist1 = 0;
	int speed = 0;
	int numb = 0;
	double r;
	double max = 0.0;;
	vector<int>v;
	cin >> num;
	double arr[num];
	for (int a = 0; a < num ; a++) {
		cin >> dist;
		cin >> numb;

		while (numb > 0) {
			cin >> dist1;
			v.push_back(dist1);
			cin >> speed;
			v.push_back(speed);
			numb--;
		}
		for (int b = 0; b < v.size(); b+=2) {
			if ((double)(dist-v[b])/v[b+1] > max) {
				max = (double)((dist - v[b]) / v[b + 1]);
			
			}
		}

		arr[a]=dist / max;
	max=0.0;
		v.clear();
	}
	cout<<fixed;
cout<<setprecision(6);	
	for (int c = 0; c < num; c++) {
		cout << "Case #" << c + 1 << ": " <<arr[c] << endl;
	}
	return 0;
}
