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
	freopen("tt.txt","r",stdin);
	freopen("gcj_2017_out_b1.txt","w",stdout);
	int cno=1;
	CASE{
		
		ll n,a[100],j,i,k;
		cin>>n;
		i=-1;
		while(n!=0){
			a[++i] = n%10;
			n/=10;
		}
		j=0,k=i;
		while(j<k){
			swap(a[j],a[k]);
			j++;
			k--;
		}
		for(j=i-1;j>=0;j--){
			if(a[j]>a[j+1]){
				a[j]--;
				for(k=j+1;k<=i;k++)
				a[k]=9;
			}
		}
		k=0;
		while(a[k]==0)
		k++;
		cout<<"Case #"<<cno++<<": ";
		for(j=k;j<=i;j++){
			cout<<a[j];
		}
		cout<<endl;
	}
    return 0;
}

