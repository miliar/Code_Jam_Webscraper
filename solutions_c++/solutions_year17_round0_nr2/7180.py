#include <bits/stdc++.h>
using namespace std;

#define INT(x) (int)(x - '0')
#define CHAR(x) (int)(x + '0')
#define LL long long

int main(){


  ios_base::sync_with_stdio(false);
  #ifndef ONLINE_JUDGE
  freopen("input.in","r",stdin);
  freopen("output.out","w",stdout);
  #endif

  int t,test=1,n;
  cin>>t;
  while(t--){
  	string A;
  	cin>>A;
  	n = A.size();
  	if(n == 1){
  		cout<<"Case #"<<test++<<": "<<A<<endl;
  		continue;
  	}

  	string ans;

  	bool zeroIndex = false;
  	for(int i=1;i<n;i++){
  		if(INT(A[i-1]) == 1 && INT(A[i]) == 0){
  			zeroIndex = true;
  			break;
  		}
  	}

  	if(zeroIndex){
  		if(INT(A[0]) == 1){
  			for(int i=0;i<n-1;i++)
  				ans = ans + '9';
  		}else{
  			ans = to_string(INT(A[0]) - 1);
  			for(int i=0;i<n-1;i++)
  				ans = ans + '9';
  		}
  	}else{
  		int prev = INT(A[0]);
  		int prevIndex = 0;
  		bool flag = false;
  		for(int i=1;i<n;i++){
  			if(INT(A[i]) >= prev){
  				prev = INT(A[i]);
  				prevIndex = i;
  			}else{
  				flag = true;
  				break;
  			}
  		}
  		while(prevIndex > 0 and INT(A[prevIndex]) == INT(A[prevIndex-1]))
  			prevIndex--;
  		if(!flag)
  			ans = A;
  		else{
  			if(prevIndex == 0 && prev == 1){
  				for(int i=0;i<n-1;i++)
  					ans  = ans + '9';
  			}else{
  				for(int i=0;i<prevIndex;i++)
  					ans = ans + A[i];
  				ans = ans + to_string(INT(A[prevIndex]) - 1);
  				for(int i=prevIndex+1;i<n;i++)
  					ans = ans + '9';
  			}
  		}
  	}
  	cout<<"Case #"<<test++<<": "<<ans<<endl;
  }
  return 0;
}