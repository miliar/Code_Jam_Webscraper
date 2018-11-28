/* 
	author: Bhrigu Gupta
		aka “bhrigudov”
*/

#include <bits/stdc++.h>

using namespace std;

#define fo(i,a,b) for(i=a;i<b;i++)
#define rf(i,b,a) for(i=b; i>=a; i--)

typedef long long ll;

int main(int argc, char const *argv[])
{
	ios_base::sync_with_stdio(false); 

	ll n, i, t, k, pos, pos2, len;
	int s[25];

	cin>>t;
	fo(k,1,t+1)
	{
		cin>>n;

		len = 0;
		pos = -1;

		while(n) {
			s[len] = n%10;
			n/=10;
			len++;
		}

		rf(i, len-2, 0) {
			if(s[i]<s[i+1]) {
				pos = i+1;
				break;
			}
		}

		pos2 = pos;
		if(pos!=-1) {
			if(s[pos2]==1) {
				rf(i, len-2, pos2) s[i] = 9;
				s[len-1] = 0;
			}
			else {
				do {
					s[pos2] = s[pos2]--;
					pos2++;
				} while(pos2<len && s[pos2]>s[pos2-1]);
			}
		}

		rf(i,pos-1,0) s[i] = 9;

		if(s[len-1]==0) len--;
		cout<<"Case #"<<k<<": ";
		rf(i, len-1, 0) cout<<s[i];
		cout<<"\n";
	}

	return 0;
}