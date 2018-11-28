#include <bits/stdc++.h>
using namespace std;

int main(){


  ios_base::sync_with_stdio(false);
  #ifndef ONLINE_JUDGE
  freopen("input.in","r",stdin);
  freopen("output.out","w",stdout);
  #endif

  int t,test = 1;
  cin>>t;
  while(t--){
  	int n,k;
  	string A;
  	cin>>A;
  	cin>>k;
  	n = A.size();
  	int left = -1;
  	for(int i=0;i<n;i++){
  		if(A[i] == '-'){
  			left = i;
  			break;
  		}
  	}

  	if(left == -1){
  		cout<<"Case #"<<test++<<": 0"<<endl;
  		continue;
  	}
  	int ans = 0;
  	while(left + k <= n){
  		for(int i=left;i<left+k;i++){
  			if(A[i] == '-')
  				A[i] = '+';
  			else
  				A[i] = '-';
  		}
  		while(A[left] == '+' && left < n)
  			left++;
  		ans++;
  	}
  	if(left == n){
  		cout<<"Case #"<<test++<<": "<<ans<<endl;
  	}else{
  		cout<<"Case #"<<test++<<": IMPOSSIBLE"<<endl;
  	}
  }
  return 0;
}