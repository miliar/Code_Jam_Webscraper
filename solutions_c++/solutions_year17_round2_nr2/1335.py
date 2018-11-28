#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<vector>
#include<queue>
#include<algorithm>
#include<math.h>
#include<map>
#include<stack>
#include<string.h>
#define STOP system("pause")
#define bits(num) __builtin_popcount(num)
#define CASE int t;scanf("%d",&t);while(t--)
#define ll long long int
#define lu unsigned long long
#define MAX(a,b) a>b?a:b
#define MIN(a,b) a<b?a:b
using namespace std;
int main()
{
	freopen("zz.in","r",stdin);
	freopen("gcj_1b1_a_out211.txt","w",stdout);
	int tno=1;
	CASE{
		int n,R,Y,B,O,G,V;
		cout<<"Case #"<<tno++<<": ";
		cin>>n;
		cin>>R>>O>>Y>>G>>B>>V;
		if(R>Y+B||Y>B+R||B>Y+R){
			cout<<"IMPOSSIBLE"<<endl;	
			continue;
		}
		string str="";
		while(R||Y||B){
			if(str[str.size()-1] =='R'){
				if(Y>B){
					Y--;
					str+='Y';				
				}
				else{
					B--;
					str+='B';
				}
			}
			else if(str[str.size()-1]=='Y'){
				if(R>B){
					R--;
					str+='R';
				}
				else{
					B--;
					str+='B';
				}
			}
			else{
				if(R>Y){
					R--;
					str+='R';
				}
				else{
					Y--;
					str+='Y';
				}
			}
		}
		int i,j;
		string str1="";
		if(str[0]==str[str.size()-1]){
			for(i=1;i<n-1;i++){
				if(str[i]!=str[str.size()-1]&&str[i+1]!=str[str.size()-1]){
					for(j=0;j<=i;j++)
					str1+=str[j];
					
					str1+=str[str.size()-1];
					
					for(j=i+1;j<n-1;j++)
					str1+=str[j];
					
					break;
				}
			}
			cout<<str1<<endl;
			continue;
		}
		cout<<str<<endl;
		
	}
    return 0;
}

