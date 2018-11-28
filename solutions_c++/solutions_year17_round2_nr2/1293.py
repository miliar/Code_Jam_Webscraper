#include<bits/stdc++.h>
using namespace std;

vector< pair< int, char > > vec;
char str[1010],ans[1010];

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,n,ti,i,j,k,r,g,b,o,y,v,ext,R,Y,B,l;
    scanf("%d",&t);
    for(ti=1; ti<=t; ++ti)
    {
        R=Y=B=0;
        scanf("%d",&n);
        scanf("%d %d %d",&r,&o,&y);
        scanf("%d %d %d",&g,&b,&v);
        r-=g;
        y-=v;
        b-=o;
        vec.clear();
        vec.push_back( {r,'R'});
        vec.push_back( {y,'Y'});
        vec.push_back( {b,'B'});
        sort(vec.begin(),vec.end());
        if(vec[0].first+vec[1].first<vec[2].first)
            printf("Case #%d: IMPOSSIBLE\n",ti);
        else
        {
            //printf("%d %d %d\n",vec[0].first,vec[1].first,vec[2].first);
            j=0;
            ext=vec[0].first+vec[1].first-vec[2].first;
            for(i=0; i<vec[2].first; ++i)
            {
                str[j++]=vec[2].second;
                if(vec[1].first>0)
                {
                    str[j++]=vec[1].second;
                    vec[1].first--;
                    if(ext>0)
                    {
                        str[j++]=vec[0].second;
                        ext--;
                    }
                }
                else
                    str[j++]=vec[0].second;


            }
            str[j]=0;
            k=0;
            for(i=0; i<j; ++i)
            {
                if(str[i]=='R' && g)
                {
                    for(l=0; l<g; ++l)
                        ans[k++]='R',ans[k++]='G';
                    ans[k++]='R';
                    g=0;
                }
                else if(str[i]=='Y' && v)
                {
                    for(l=0; l<v; ++l)
                        ans[k++]='Y',ans[k++]='V';
                    ans[k++]='Y';
                    v=0;

                }
                else if(str[i]=='B' && o)
                {
                    for(l=0; l<o; ++l)
                        ans[k++]='B',ans[k++]='O';
                    ans[k++]='B';
                    o=0;

                }
                else
                    ans[k++]=str[i];
            }

            if( g)
            {
                for(l=0; l<g; ++l)
                    ans[k++]='R',ans[k++]='G';

                g=0;
            }
            if(v)
            {
                for(l=0; l<v; ++l)
                    ans[k++]='Y',ans[k++]='V';

                v=0;

            }
            if(o)
            {
                for(l=0; l<o; ++l)
                    ans[k++]='b',ans[k++]='O';

                o=0;

            }
            ans[k]=0;
            printf("Case #%d: %s\n",ti,ans);
        }
    }
    return 0;
}
