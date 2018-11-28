#include <bits/stdc++.h>

using namespace std;
#define ll long long
template<class T> void p(vector<T>& a){ for(int i = 0;i < a.size();i++) cout << a[i] << " "; cout << endl; }
#define vi vector<int>
#define vl vector<ll>
#define vb vector<bool>
#define f(i,a,b) for(auto i = a;i < b;i++)

void enhance1(string& s,int ab){
	s[ab] -= 1;
	f(i,ab + 1,s.size()){
		s[i] = '9';
	}
	return;
}

void enhance2(string& s){
	if(s[0] == '1' ){
		s.resize(s.size() - 1);
		s[0] = '9';
	}
	else s[0] -= 1;
	f(i,1,s.size()){
		s[i] = '9';
	}
}

int main(){
	int t,k,i,j;
	cin >> t;
	f(t_,0,t){
		ll num;
		string s;
		cin >> num;
		cout << s;
		stringstream stream;
		stream << num;
		stream >> s;
		//cout << s;
		bool flag = false;
		for(i = 0;i < s.size() - 1;i++){
			if(s[i] > s[i + 1]){
				flag = true;
				break;
			}
		}
		if(flag){
			//cout << i << endl;
			bool f = false;
			for(j = i;j >= 1;j--){
				if(s[j] > s[j - 1]){
					f = true;
					break;
				}
			}
			if(f){
				enhance1(s,j);
			}
			else{
				enhance2(s);
			}
		}
		cout << "Case #" << t_ + 1 << ": " <<  s << endl;
		}
	return 0;
}



