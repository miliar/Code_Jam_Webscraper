#include <bits/stdc++.h>
using namespace std;

int main() {
	
	int Test;
	cin>>Test;
	for(int m=1;m<=Test;m++){
	    cout<<"Case #"<<m<<": ";
	string str;
	cin>>str;
	int k;
	cin>>k;
	
	int N=str.size();
    int *arr=new int [N];
    for (int i = 0; i < N; i++) {
        /* code */
        arr[i]= (str[i]=='+') ? 1 : 0; 
    }
    
	int i=0,j,count=0;
	bool flag=false;
	while(i<N){ // increment i
    
        while(i<N && arr[i]) i++;
        j=i;
        
        if(j<=N-k) {
            for (int p = 0; p < k; p++) {
                /* code */
                arr[j+p]^=1;
            }
            count++;
        }else if(j<N){
          flag=true;  
        }
	    
	    i=j+1;
	    
	}
	if(flag)
	    cout<<"IMPOSSIBLE"<<endl;
	else
	    cout<<count<<endl;
	
	}
	return 0;
}

