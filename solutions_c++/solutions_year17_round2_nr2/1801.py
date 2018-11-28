#include <bits/stdc++.h>
using namespace std;
void swap(int *max, char * m,int a, int b)
{
    int temp = max[a];
    max[a] = max[b];
    max[b] = temp;
    char t = m[a];
    m[a] = m[b];
    m[b] = t;
}
void Sort(int *max, char * m, int l , int r)
{
    if(r-l<=1)
    return;
    int y = l+1, g = l+1;
    for(;g<r;g++)
    {
        if(max[g] > max[l])
        {
            swap(max,m,g,y);
            y++;
        }
        
    }
    swap(max,m,l,y-1);
    Sort(max,m,l,y);
    Sort(max,m,y+1,r);
}
void fun(int *max,char *m)
{
    if(max[1] + max[2] < max[0])
    {
        cout<<"IMPOSSIBLE";
        return;
    }
    int i,j;
    for(i=0,j=0;i<max[0];i++)
    {
        cout<<m[0];
        if(j<max[1])
        {
            cout<<m[1];
            j++;
        }
        if(i>=max[0] - max[2])
        cout<<m[2];
    }
}
int main() 
{
	int T,Case = 1;
	cin >> T;
	while(T--)
	{
	    int n,r,o,y,g,b,v;
	    cin>>n>>r>>o>>y>>g>>b>>v;
	    int max[3];
	    char m[3] = {'R','Y','B'};
	    max[0] = r;
	    max[1] = y;
	    max[2] = b;
	    Sort(max,m,0,3);
	    cout<<"Case #"<<Case<<": ";
	    fun(max,m);
	    cout<<endl;
	    
	    Case++;
	}
	return 0;
}
