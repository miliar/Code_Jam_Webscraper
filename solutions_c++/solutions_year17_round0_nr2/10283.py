//
//  GCJQRpB.cpp
//  
//
//  Created by 楊承昊 on 2017/4/8.
//
//

#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios::sync_with_stdio(0);cin.tie(0);
    int T;
    cin>>T;
    for(int TEST=1;TEST<=T;TEST++)
    {
        char enter[20]={0};
        cin>>enter;
        int strn=strlen(enter),tran[20]={0},clean=0,judge=0;
        for(int i=0;i<strn;i++)
        {
            tran[i]=enter[i]-'0';
        }
        while(judge==0)
        {
            judge=1;
            int findmin=0;
            for(int i=clean;i<strn;i++)
            {
                if(findmin>tran[i]) judge=0;
                else findmin=max(findmin,tran[i]);
            }
            if(judge)
            {
                cout<<"Case #"<<TEST<<": ";
                for(int i=clean;i<strn;i++)
                    cout<<tran[i];
                cout<<endl;
            }
            else
            {
                for(int i=strn-1;i>=clean+1;i--)
                {
                    int qwe=tran[i-1]*10+tran[i];
                    int leg=1;
                    while(leg)
                    {
                        if(qwe/10>qwe%10)
                        {
//                            if(qwe/10 > (qwe-1)/10 &&i==clean+1) tran[i+1]+=10;
                            qwe--;
                            if(i+1<strn) tran[i+1]=9;
                        }
                        else
                            leg=0;
                    }
//                    cout<<qwe<<endl;
                    tran[i-1]=qwe/10;
                    tran[i]=qwe%10;
                }
//                for(int i=clean;i<strn;i++)
//                    cout<<tran[i];
//                cout<<endl;
                if(tran[clean]==0)
                {
                    clean++;
                    tran[clean+2]=9;
                }
            }
        }
    }
    return 0;
}
