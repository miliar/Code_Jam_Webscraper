#define _CRT_SECURE_NO_WARNINGS
#include<set>
#include<string>
#include<iostream>
#include<algorithm>
#define FASTME ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
using namespace std;
#define int long long int
int a[1001];
bool isTidy(int n){
	string s = std::to_string(n);
	string t(s);
	sort(t.begin(), t.end());
	return t == s;
}
void process(){
	int x = 0;
	int no = 0;
	while (x < 1001){
		if (isTidy(no)){
			a[x++] = no;
		}
		++no;
	}
}
#undef int
int main() {
	FASTME
	#ifdef _DEBUG
	freopen("c:/in.txt", "r", stdin);
	freopen("c:/out.txt", "w", stdout);
	#endif
#define int long long int
	process();
	int T;
	cin >> T;
	for (int i = 1; i <= T; ++i){
		int x = 0;
		int N; cin >> N;
		for (x = 0; a[x] <= N; ++x);
		if (a[x] > N)--x;
		cout << "Case #" << i << ": " << a[x] << endl;
	}
	return 0;
}