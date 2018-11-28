#include <bits/stdc++.h>
using namespace std;

#define IN_FILE "input1.in"
#define OUT_FILE "outL4.txt"

char s1[100][100];
int mar[100];

int main() {
	ios::sync_with_stdio(0);
	ifstream xin(IN_FILE);
	ofstream xout(OUT_FILE);
	cin.rdbuf(xin.rdbuf());
	cout.rdbuf(xout.rdbuf());
	int i,j,t1,t2,t3,t4,t,r,c,cnt=0,k1,k2,k3,k4;
	cin>>t;
	while(t--){
	    cin>>r>>c;
	    for(i=0;i<r;i++){
	        cin>>s1[i];
	        mar[i]=-1;
	    }
	    cnt++;
	    cout<<"Case #"<<cnt<<":\n";
	    for(i=0;i<r;i++){
	        t1=0;
	        for(j=0;j<c;j++){
	            if(s1[i][j]=='?')
	                t1++;
	            if(s1[i][j]!='?'){
	               mar[i]=1;
	               for(k1=j+1;k1<c;k1++){
	                   if(s1[i][k1]=='?')
	                       s1[i][k1]=s1[i][j];
	                   else
	                       break;
	               }
	               for(k1=j-1;k1>=0;k1--){
	                   if(s1[i][k1]=='?')
	                       s1[i][k1]=s1[i][j];
	                   else
	                       break;
	               }
	            }
	        }
	    }
	    for(i=0;i<r;i++){
	        if(mar[i]==1){
	            for(j=i-1;j>=0;j--){
	                if(mar[j]==-1){
	                    mar[j]=1;
	                    strcpy(s1[j],s1[i]);
	                }
	                else
	                    break;
	            }
	            for(j=i+1;j<r;j++){
	                if(mar[j]==-1){
	                    mar[j]=1;
	                    strcpy(s1[j],s1[i]);
	                }
	                else
	                    break;
	            }
	        }
	    }
	    for(i=0;i<r;i++){
	        cout<<s1[i]<<endl;
	    }
	}
	return 0;
}

