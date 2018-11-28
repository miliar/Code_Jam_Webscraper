#include <iostream>
#include <fstream>
using namespace std;

int main()
{
int t=1,n,k,a[1002],j,start,dist,last,beg,mx,nw,ls,rs,x;
    cin>>t;
	for(int i=1;i<=t;i++)
	{
	    cin>>n>>k;
	    a[0]=2;
	    a[n+1]=2;
	    for(j=1;j<=n;j++)
	    {
                a[j]=0;
	    }

	    for(x=1;x<=k;x++)
        {
              dist = 0;
            mx = 0;
             start = 0;

            for(j=1;j<n+2;j++)
            {
                if(a[j]>0)
                {
                    dist=j-start;
                    if(dist>mx)
                    {
                         beg = start;
                        last = j;
                        mx = dist;
                    }
                    start=j;
                }
            }
            nw = (beg + last)/2;
            a[nw] = 1;


        }
        ls = nw - (beg+1);
        rs = last - (nw+1);

        cout<<"Case #"<<i<<": "<<rs<<" "<<ls;
        cout<<endl;
	}

    return 0;
}
