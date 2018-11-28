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

const int MAXN = 1e6 + 10;
ll po[30], cnt[MAXN];

inline int calc(ll n, ll k){
	cnt[n] ++;
	k --;
	int tedad = 0, ptr = n;
	while(ptr > 0 and tedad < k){
		while(ptr > 0 and cnt[ptr] == 0) ptr --;
		if(ptr > 0){
			while(tedad < k and cnt[ptr] > 0){
				int a1 = ptr / 2, a2 = (ptr + 1) / 2 - 1;
				cnt[ptr] --;
				cnt[a1] ++; cnt[a2] ++;
				tedad ++;
			}
		}
	}

	int mn = 0, mx = 0;
	for(int i = 0; i <= ptr; i ++){
		if(cnt[i]) mx = i;
		cnt[i] = 0;
	}
	return mx;
}


int main(){
	ios::sync_with_stdio(false); cin.tie(0);
	ifstream fin("salam2.txt");
	ofstream fout("salam.txt");
	int t; fin >> t;
	for(int i = 0; i < t; i ++){
		int n, k; fin >> n >> k;
		int ans = calc(n, k), a1 = ans / 2, a2 = (ans + 1) / 2 - 1;
		fout << "Case #" << i + 1 << ": " << a1 << ' ' << a2 << endl;
	}
	//system("pause");
	return 0;	
}