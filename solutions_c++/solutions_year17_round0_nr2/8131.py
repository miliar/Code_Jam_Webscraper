#include <bits/stdc++.h>
using namespace std;
int n;
int tip[100];
bool check(int x)
{
	int num;
	num=0;
	while (x>0){
		num++;
		tip[num]=x%10;
		x/=10;
	}
	//help=true;
	for (int i=num;i>=2;i--){
		if (tip[i]>tip[i-1]) return false;
	}
	return true;
	//if flag
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t,cas=0;
	scanf("%d",&t);
	while (t--){
		cas++;
		scanf("%d",&n);
		for (int i=n;i>=1;i--){
			if (check(i)){
				printf("Case #%d: %d\n",cas,i);
				break;
			}
		}
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
} 
