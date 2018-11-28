#pragma GCC optimize "Ofast,omit-frame-pointer,inline"
#include <bits/stdc++.h>
using namespace std;

string s;
int k;
int INF = 1e9;

int findMin(int i){
	if(i<k-1){	//we can't flip anymore
		for(int j=0;j<=i;j++)
			if(s[j]=='-')
				return INF;	//there is a blank face
		return 0;	//no need to flip
	}
	//we can flip
	if(s[i]=='-') //we must flip
	{
		for(int j=0;j<k;j++)
			s[i-j] = s[i-j]=='-'?'+':'-';
		return 1+findMin(i-1);
	}
	else{	//we must not flip
		return findMin(i-1);
	}

	return INF;
}

int main(){
    ios::sync_with_stdio(false);
    freopen("gcj1input.in","r",stdin);
    freopen("output1large.txt","w",stdout);
    int t,ans1,ans2,ans,c=1;
    string S;
    cin>>t;
    while(t--){
    	cin>>S>>k;
    	s = S;
    	ans1 = findMin(s.length()-1);
    	reverse(S.begin(),S.end());
    	s = S;
    	ans2 = findMin(s.length()-1);
    	ans = min(ans1,ans2);
    	cout<<"Case #"<<c++<<": ";
    	if(ans >= INF)
    		cout<<"IMPOSSIBLE"<<endl;
    	else cout<<ans<<endl;
    }
	return 0;
}