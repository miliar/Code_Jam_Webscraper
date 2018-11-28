#include <stdio.h>

FILE* in=fopen("D-large.in","r");
FILE* out=fopen("D-large.out","w");

int map[101][101];
int upg[101][101];
int emptyR[101],emptyC[101];
int emptyD1[201],emptyD2[201];
int mt[2][100],st[2],fn[2];

void solve()
{
	int n,m,i,r,c,t;
	char ch;
	fscanf(in,"%d %d",&n,&m);
	for(r=1;r<=n;r++)
	{
		for(c=1;c<=n;c++)
		{
			upg[r][c]=map[r][c]=0;
			emptyD1[r+c]=1;
			emptyD2[r-c+n]=1;
		}
		emptyR[r]=emptyC[r]=1;
	}
	int ans=0;
	for(i=0;i<m;i++)
	{
		fscanf(in," %c %d %d",&ch,&r,&c);
		if(ch=='+') t=1;
		if(ch=='x') t=2;
		if(ch=='o') t=3;
		map[r][c]=t;
		emptyR[r]&=(t==1);
		emptyC[c]&=(t==1);
		emptyD1[r+c]&=(t==2);
		emptyD2[r-c+n]&=(t==2);
		
		ans+=1;
		ans+=(t==3);
	}
	m=0;
	for(r=1,c=1;r<=n;r++) if(emptyR[r])
	{
		while(c<=n && !emptyC[c]) c++;
		if(c>n) break;
		ans++;
		m++;
		upg[r][c++]+=2;
	}
	
	if(emptyD1[n+1])
	{
		ans++;
		m+=!upg[n][1];
		upg[n][1]+=1;
	}
	if(n>1 && emptyD2[n])
	{
		ans++;
		m+=!upg[1][1];
		upg[1][1]+=1;
	}
	
	st[0]=fn[0]=st[1]=fn[1]=0;
	for(i=2;i<n;i++)
	{
		t=(i%2);
		if(emptyD1[n+2-i]) mt[t][fn[t]++]=n+2-i;
		if(emptyD1[n+i]) mt[t][fn[t]++]=n+i;
		if(emptyD2[i] && st[t]<fn[t])
		{
			int add=mt[t][st[t]++];
			int sub=i-n;
			r=(add+sub)/2;
			c=(add-sub)/2;
			
			ans++;
			m+=!upg[r][c];
			upg[r][c]+=1;
		}
		if(emptyD2[2*n-i] && st[t]<fn[t])
		{
			int add=mt[t][st[t]++];
			int sub=n-i;
			r=(add+sub)/2;
			c=(add-sub)/2;
			
			ans++;
			m+=!upg[r][c];
			upg[r][c]+=1;
		}
	}
	
	fprintf(out,"%d %d %c",ans,m,'\n');
	
	for(r=1;r<=n;r++) for(c=1;c<=n;c++) if(upg[r][c])
	{
		t=upg[r][c]+map[r][c];
		if(t==1) ch='+';
		if(t==2) ch='x';
		if(t==3) ch='o';
		fprintf(out,"%c %d %d %c",ch,r,c,'\n');
	}
}

int main()
{
	int i,T;
	fscanf(in,"%d",&T);
	for(i=1;i<=T;i++)
	{
		fprintf(out,"Case #%d: ",i);
		solve();
	}
}
