#include <bits/stdc++.h>
using namespace std;
typedef struct{
    long long int r, h;
} cake;

int cmp(const void * a, const void * b)
{

  cake *orderA = (cake *)a;
  cake *orderB = (cake *)b;
  double bh = (orderB->h)*(orderB->r);
  double ah = (orderA->h)*(orderA->r);
    if( bh > ah )
        return 1;
    if( ah > bh )
        return -1;
    else return 0;
}

int main() {
	ios::sync_with_stdio(false);
	long long int i, t, tt, n, k, max, in, flag, maxr, bi;
	double area, temp, base, maxx, newh, last;
	cin>>t;
	for(tt=1; tt<=t; tt++)
	{
	    area = max = in = flag = 0;
	    cin>>n>>k;
	    cake a[n];
	    for(i=0; i<n; i++)
	        cin>>a[i].r>>a[i].h;
	    /*for(i=0; i<n; i++)
	    {
	        if(a[i].r > max)
	        {
	            max = a[i].r;
	            in = i;
	        }
	        if(a[i].r == max && a[i].h > a[in].h)
	        {
	            max = a[i].r;
	            in = i;
	        }
	    }*/
	    qsort(a, n, sizeof(cake), cmp);
	    //for(i=0; i<n; i++)
	        //cout<<a[i].r<<"\n";
	    maxr = base = bi = 0;
	    for(i=0; i<k; i++)
	    {
	        area += 2*3.14159265359*(a[i].r)*(a[i].h);
	        if(a[i].r > maxr)
	        {
	            base = 3.14159265359*(a[i].r)*(a[i].r);
	            maxr = a[i].r;
	        }
	    }
	    /*if(flag==0)
	    {
	        area += 2*3.14159265359*(a[in].r)*(a[in].h);
	        area -= 2*3.14159265359*(a[k-1].r)*(a[k-1].h);
	    }*/
	    area += base;
	    maxx = 0;
	    in = k;
	    for(i=k; i<n; i++)
	    {
	        temp = 3.14159265359*(a[i].r)*(a[i].r);// + 2*3.14159265359*(a[i].h)*(a[i].r);
	        if(temp>maxx)
	        {
	            in = i;
	            maxx = temp;
	        }
	    }
	    newh = 2*3.14159265359*(a[in].h)*(a[in].r);
	    last = 2*3.14159265359*(a[k-1].h)*(a[k-1].r);
	    if((maxx-base)>(last - newh))
	    {
	        //cout<<"max="<<maxx<<" base="<<base<<" last="<<last<<" newh="<<newh<<"\n";
	        area += maxx;
	        area -= last;
	        area -= base;
	        area += newh;
	    }
	    cout<<"Case #"<<tt<<": "<<fixed<<setprecision(9)<<area<<"\n";
	}
	return 0;
}
