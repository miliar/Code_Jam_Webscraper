#include <iostream>
#include <set>
#include <algorithm>
using namespace std;
#include <queue>
#include <vector>
#include <fstream>

ifstream fin("C-small-1-attempt0.in");
ofstream fout("output.txt");

#define cin fin
#define cout fout


bool cmp(pair<int, int> a, pair<int, int> b)
{
	if(a.second < b.second)
		return true;
	else if(b.second < a.second)
		return false;
	if(a.first < b.first)
		return true;
	return false;
}

int main()
{
	vector<pair<int, int> > vec;
	int n, k, t;
	cin >> t;
	int b, c;
	for(int i = 0; i < t; i++){
		cin >> n >> k;
		priority_queue<int, vector<int> > pq;
		pq.push(n);
		for(int j = 0; j < k; j++){
			int a = pq.top();
			pq.pop();
			b = a / 2, c = a / 2;
			if(a % 2 == 0)
				c--;
			pq.push(b);
			pq.push(c);
			//cout << a << " " << b << " " << c << "\n";
		}
		cout << "Case #" << i + 1 << ": " << b << " " << c << "\n";
	}
	fout.close();
}