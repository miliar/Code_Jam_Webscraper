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
	freopen("gcj_2017_in_a1.txt","r",stdin);
	freopen("gcj_2017_out_a1.txt","w",stdout);
	int cno=1;
	CASE{
		string s;
		int i,j,n,flag=0;
		cin>>s>>n;
		int len = s.size(),cnt=0;
		for(i=0;i<=len-n;i++){
			if(s[i]=='+')
			continue;
			for(j=i;j<i+n;j++){
				if(s[j]=='+')
				s[j]='-';
				else
				s[j]='+';
			}
			cnt++;
		}
		for(i=0;i<len;i++)
		if(s[i]=='-')
		flag++;
		cout<<"Case #"<<cno++<<": ";
		if(flag){
			cout<<"IMPOSSIBLE"<<endl;
		}
		else{
			cout<<cnt<<endl;
		}	
		
	}
    return 0;
}

