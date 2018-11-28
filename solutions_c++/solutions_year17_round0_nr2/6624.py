#include <bits/stdc++.h>
using namespace std;

int main() {
    int test;
    cin>>test;
    for(int p=0;p<test;p++){
	char a[20];
	cin>>a;
	vector<int> v;
	int i=0,num,flag=0;
	for(i=0;a[i]!='\0';i++){
	    num=a[i]-'0';
	    v.push_back(num);
	}
	if(i!=1){
	    while(1){
	for(int j=0;j<v.size()-1;j++){
	    if(j==0&&(v[0]>v[1])){
	        v[0]=v[0]-1;
	        for(int k=1;k<v.size();k++){
	            v[k]=9;
	        }
	    }else{
	        if(v[j]>v[j+1]){
	            if(v[j]==0){
	                v[j]=9;
	            }else{
	                v[j]=v[j]-1;
	            }
	            for(int k=j+1;k<v.size();k++){
	                v[k]=9;
	            }
	        }
	    }
	}
	for(int k=0;k<v.size()-1;k++){
	    if(v[k]>v[k+1]){
	        flag=1;
	        break;
	    }
	}
	if(flag==0){
	    break;
	}
	flag=0;
	    }
	}else{
	    cout<<"Case #"<<p+1<<": ";
	    cout<<a;
	    if(p+1<test){
	    cout<<endl;
	    }
	    flag=2;
	}
	if(flag!=2){
	    cout<<"Case #"<<p+1<<": ";
	    for(int k=0;k<v.size();k++){
	        if(k==0){
	            if(v[0]!=0){
	                cout<<v[k];
	            }
	        }else{
	                cout<<v[k];
	        }
	            }
	            if(p+1!=test){
	                cout<<endl;
	            }
	}
    }
	return 0;
}
