#include <bits/stdc++.h>

using namespace std;
#define ll long long
template<class T> void p(vector<T>& a){ for(int i = 0;i < a.size();i++) cout << a[i] << " "; cout << endl; }
#define vi vector<int>
#define vl vector<ll>
#define vb vector<bool>
#define f(i,a,b) for(auto i = a;i < b;i++)

int main(){
	int t,k;
	cin >> t;
	f(t_,0,t){
		string s;
		cin >> s >> k;
		vb arr(s.size());
		f(i,0,s.size()){
			if(s[i] == '-')
				arr[i] = 0;
			else
				arr[i] = 1;
		}
		int count = 0;
		f(i,0,s.size() - k){
			if(!arr[i]){
				for(int j = 0;j < k;j++){
					arr[i + j] = !arr[i + j];
				}
				count++;
			}
		}
		//p(arr);
		int i = s.size() - k;
		bool flag = true;
		for(;i < s.size() - 1;i++){
			if(arr[i] != arr[i + 1]){
				flag = false;
				break;
			}
		}
		if(flag){
			if(!arr[i]) count++;
			cout << "Case #" << t_ + 1 << ": " << count << endl;
		}
		else{
			cout << "Case #" << t_ + 1 << ": IMPOSSIBLE\n";
		}
	}
	return 0;
}
