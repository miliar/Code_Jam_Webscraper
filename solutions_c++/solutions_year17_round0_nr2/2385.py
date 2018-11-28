
#include<bits/stdc++.h>
using namespace std;
#define D(x)	cout << #x " = " << (x) << endl
#define MAX		25

char str[MAX], nmb[MAX];
int n;

void brute(int pos, int flag)
{
	if(pos > n) return;
	
	if(flag == true){
		nmb[pos] = '9';
		return brute(pos + 1, flag);
	}
	else
	{
		char curr = str[pos]; 
		int p;
		
		for(p = pos; p <= n; p++)
			if(str[p] != curr) break; 
			
		if(p > n || str[p] > curr){
			nmb[pos] = curr; 
			return brute(pos + 1, flag);
		}
		else{
			nmb[pos] = curr - 1;
			return brute(pos + 1, true); 
		}
	}
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout); 
	
	int t, cs;
	
	scanf("%d", &t);
	for(cs = 1; cs <= t; cs++)
	{
		memset(nmb, 0, sizeof(nmb));
		
		scanf("%s", str + 1);		
		n = strlen(str + 1); 
		
		printf("Case #%d: ", cs);
		brute(1, false);
		int p = 1; 
		while(nmb[p] == '0') p++;
		puts(nmb + p); 
	}
	return 0;
}
