// In the name of Allah
// #Isart

#include<bits/stdc++.h>

#define pii pair<int, int>
#define pb push_back
#define F first
#define S second
#define ll long long
#define ld long double

using namespace std;

const int MAXN = 1e5 + 10;
int a[MAXN], cnt[MAXN];

int main(){
	ios::sync_with_stdio(false); cin.tie(0);
	ifstream fin("salam2.txt");
	ofstream fout("salam.txt");
	int n; fin >> n;
	for(int i = 0; i < n; i ++){
		string s;
		fin >> s;
		int k;
		fin >> k;
		int ans = 0, fans = 0;
		for(int j = 0; j < s.size(); j ++){
			if(s[j] == '-') a[j] = 0;
			else a[j] = 1;
			cnt[j] = 0;
		}
		bool is = true;
		for(int j = 0; j < s.size(); j ++){
			ans += cnt[j];
			a[j] = (a[j] + ans) % 2;
			if(a[j] == 0 and k + j > int(s.size())){
				is = false;
				break;
			}
			if(a[j] == 0){
				ans ++;
				fans ++;
				cnt[j + k] = -1;
			}
		}
		fout << "Case #" << i + 1 << ": ";
		if(is == false)
			fout << "IMPOSSIBLE" << endl;
		else fout << fans << endl;
	}	
	return 0;	
}