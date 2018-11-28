//
//  main.cpp
//  ProblemB
//
//  Created by 胡思源 on 2017/4/8.
//  Copyright © 2017年 胡思源. All rights reserved.
//

#include <iostream>
using namespace std;
int main(int argc, const char * argv[]) {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    int count=0;
    cin>>T;
    while (++count<=T)
    {
        string N;
        cin>>N;
        int len=N.size();
        int flag=false;
        for (int i=1;i<len;i++)
        {
            if (N[i]>=N[i-1])
                continue;
            int index=i;
            while (index>0 && N[index]<N[index-1])
            {
                N[index]='9';
                if (!flag)
                    N[index-1]--;
                index--;
            }
            flag=true;
        }
        if (N[0]=='0' && len>1)
            N.erase(N.begin());
        cout<<"Case #"<<count<<": "<<N<<endl;
    }
    return 0;
}
