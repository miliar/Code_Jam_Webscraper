#include<bits/stdc++.h>
using namespace std;
int n;
char output(int pos)
{
    if(pos==0)
        return 'R';
    if(pos==1)
        return 'O';
    if(pos==2)
        return 'Y';
    if(pos==3)
        return 'G';
    if(pos==4)
        return 'B';
    if(pos==5)
        return 'V';
}
int ans[1005];
pair<int,int>num[6];
int main()
{
    freopen("B-small-attempt2.in","r",stdin);
    freopen("B-small-attempt2.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        memset(ans,-1,sizeof(ans));
        int n;scanf("%d",&n);
        for(int i=0;i<6;i++)scanf("%d",&num[i].first);
        for(int i=0;i<6;i++)num[i].second=i;
        sort(num,num+6);
        printf("Case #%d: ",cas);
        if(num[5].first>num[4].first+num[3].first)
        {
            printf("IMPOSSIBLE\n");
            continue;
        }
        for(int i=0;i<num[5].first;i++)
        {
            ans[i*2]=num[5].second;
        }
        multiset<pair<int,int> >s;
        s.insert(make_pair(-num[3].first,num[3].second));
        s.insert(make_pair(-num[4].first,num[4].second));
        for(int i=0;i<n;i++)
        {
            if(ans[i]==-1)
            {
                pair<int,int>head=*s.begin();
                s.erase(s.begin());
                ans[i]=head.second;
                s.insert(make_pair(head.first+1,head.second));
            }
        }
        for(int i=0;i<n;i++)
            printf("%c",output(ans[i]));
        printf("\n");
//        while(1)
//        {
//            if(s.size()<=1)
//            {
//                if(s.size()==1)
//                {
//                    pair<int,int>head=*s.begin();
//                    s.erase(s.begin());
//                    printf("%c",output(head.second));
//                }
//                printf("\n");
//                break;
//            }
//            pair<int,int>fst=*s.begin();
//            s.erase(s.begin());
//            pair<int,int>scd=*s.begin();
//            s.erase(s.begin());
//            printf("%c%c",output(fst.second),output(scd.second));
//            if(fst.first<-1)
//                s.insert(make_pair(fst.first+1,fst.second));
//            if(scd.first<-1)
//                s.insert(make_pair(scd.first+1,scd.second));
//        }
    }
    return 0;
}
