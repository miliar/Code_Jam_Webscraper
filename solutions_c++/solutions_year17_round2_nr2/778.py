#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <utility>
#include <sstream>
#include <queue>
#include <cstdint>
#include <unordered_map>

using namespace std;

bool fitUnicorn(queue<string>& qu, int cnt, string str){
	while (cnt > 0){
		if (qu.size() < 2) return false;
		string str1 = qu.front(); qu.pop();
		string str2 = qu.front(); qu.pop();
		qu.push(str1 + str + str2);
		cnt--;
	}
	return true;
}


string merge(queue<string>& qu1, queue<string>& qu2, queue<string>& qu3){
	vector <string> ans(max(qu1.size(), max(qu2.size(), qu3.size())));
	queue <string> * rem1;
	queue <string> * rem2;
	queue <string> * orig;
	if (ans.size() == qu1.size()){
		rem1 = &qu2;
		rem2 = &qu3;
		orig = &qu1;
	}
	else if (ans.size() == qu2.size()){
		rem1 = &qu1;
		rem2 = &qu3;
		orig = &qu2;
	}
	else{
		rem1 = &qu1;
		rem2 = &qu2;
		orig = &qu3;
	}

	for (int i = 0; i < ans.size(); i++){
		ans[i] = orig->front(); orig->pop();
	}

	while (!rem2->empty()){
		rem1->push(rem2->front()); rem2->pop();
	}

	int it = 0;
	int n = ans.size();
	while (!rem1->empty()){
		ans[it%n] = rem1->front() + ans[it%n];
		rem1->pop();
		it++;
	}

	string output = "";
	for (int i = 0; i < ans.size(); i++){
		output = output + ans[i];
	}
	return output;
}


string getRepeat(string str, int cnt){
	string ans = "";
	for (int i = 0; i < cnt; i++){
		ans += str;
	}
	return ans;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int z = 1; z <= t; z++){
		int n;
		int r, o, y, g, b, v;
		cin >> n >> r >> o >> y >> g >> b >> v;

		queue <string> rq, yq, bq;
		for (int i = 0; i < r; i++){
			rq.push("R");
		}
		for (int i = 0; i < y; i++){
			yq.push("Y");
		}
		for (int i = 0; i < b; i++){
			bq.push("B");
		}
		bool possible = true;
		if (!(fitUnicorn(rq, g, "G") && fitUnicorn(bq, o, "O") && fitUnicorn(yq, v, "V"))){
			possible = false;
		}
		vector<int> len;
		len.push_back(rq.size());
		len.push_back(yq.size());
		len.push_back(bq.size());
		sort(len.begin(), len.end());

		if (possible && len[2] > len[1] + len[0]){
			possible = false;
		}
		string ans = "RR";
		if (possible){
			ans = merge(rq, yq, bq);
		}
		if (ans[0] == ans[ans.length()-1]) possible = false;

		if (y + v == n && y == v){
			possible = true;
			ans = getRepeat("YV", y);
		}
		else if (r + g == n && r == g){
			possible = true;
			ans = getRepeat("RG", r);
		}
		else if (o + b == n && o == b){
			possible = true;
			ans = getRepeat("OB", o);
		}

		cout << "Case #" << z << ": " << ((possible) ? ans : "IMPOSSIBLE") << endl;
	}
	return 0;
}