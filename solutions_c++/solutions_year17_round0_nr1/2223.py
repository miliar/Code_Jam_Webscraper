#include <iostream>
using namespace std;

int flips(string a, int k) {
  int m = a.length();
  int s[m]={0}; 
  int sum=0, ans=0;
  for(int i = 0; i<m; ++i)
  {
    s[i] = ( (a[i]-'0') + sum )%2 != 1; //s[i] is 1 if we need to flip starting from i
    sum += s[i] - (i >= k-1 ? s[i-k+1] : 0); 
    ans += s[i];//update answer
    if(i>m-k and s[i]!=0) return -1; //we cannot flip anymore
  }
  return ans;
}

int main() {
  freopen("A-large.in","r",stdin);
  freopen("output.txt","w",stdout);
  int t;
  cin>>t;
  for(int i = 1; i<=t; ++i)
  {
  	string a;
  	int k;
  	cin>>a>>k;
  	for(int l = 0; l<(int)a.length();++l)
  	{
  		if(a[l]=='-')
  		a[l] = '0';
  		else a[l] = '1';
  	}
 
  	int z = flips(a, k); 
  	
  	if(z==-1)
  		cout<<"Case #"<<i<<": IMPOSSIBLE\n";
  	else 
  		cout<<"Case #"<<i<<": "<<z<<"\n";

  }
return 0;
}
