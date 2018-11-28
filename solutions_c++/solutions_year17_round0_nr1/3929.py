/* 
	author: Bhrigu Gupta
		aka “bhrigudov”
*/

#include <bits/stdc++.h>

using namespace std;

#define fo(i,a,b) for(i=a;i<b;i++)

void Flip(string *s, int st, int end) {
	int i;
	fo(i, st, end) (*s)[i] == '+' ? (*s)[i]='-' : (*s)[i]='+';
}

int main(int argc, char const *argv[])
{
	ios_base::sync_with_stdio(false); 

	int n, i, j, t, k, ans, temp;
	bool flag;
	string s;

	cin>>t;
	fo(k,1,t+1)
	{
		ans = 0;
		flag = true;

		cin>>s;
		cin>>n;

		fo(i,0,s.size()-n+1) {
			if(s[i]=='-') {
				ans++;
				Flip(&s, i, i+n);
			}
		}

		fo(i,0,s.size()) if(s[i]=='-') {
							flag = false;
							break;
						}

		cout<<"Case #"<<k<<": ";
		flag ? cout<<ans : cout<<"IMPOSSIBLE";
		cout<<"\n";
	}

	return 0;
}