//
//  main.cpp
//  ProblemC
//
//  Created by 胡思源 on 2017/4/8.
//  Copyright © 2017年 胡思源. All rights reserved.
//

#include <iostream>
#include<vector>
using namespace std;
int main(int argc, const char * argv[]) {
    // insert code here...
    freopen("C-small-1-attempt0.in", "r", stdin);
    freopen("C-small-1-attempt0.out", "w", stdout);
    int T;
    int count=0;
    cin>>T;
    while (++count<=T)
    {
        int K,N;
        cin>>N>>K;
        
        vector<int> LS=vector<int>(N,0);
        vector<int> RS=vector<int>(N,0);
        
        for (int i=0;i<N;i++)
        {
            LS[i]=i;
            RS[i]=N-i-1;
        }
        
        for (int i=0;i<K;i++)
        {
            int minLR=INT_MIN;
            int maxLR=INT_MIN;
            int target=0;
            for (int j=0;j<N;j++)
            {
                if (min(LS[j],RS[j])>=minLR)
                {
                    if (min(LS[j],RS[j])==minLR)
                    {
                        if (maxLR<max(LS[j],RS[j]))
                        {
                            maxLR=max(LS[j],RS[j]);
                            target=j;
                        }
                    }
                    else
                    {
                        maxLR=max(LS[j],RS[j]);
                        target=j;
                    }
                    minLR=min(LS[j],RS[j]);
                }
            }
            
            if (i==K-1)
            {
                cout<<"Case #"<<count<<": "<<maxLR<<" "<<minLR<<endl;
            }
            else
            {
                for (int j=0;j<N;j++)
                {
                    if (target<=j)
                        LS[j]=j-target-1<LS[j]?j-target-1:LS[j];
                    if (target>=j)
                        RS[j]=target-j-1<RS[j]?target-j-1:RS[j];
                }
            }
        }
    }
    return 0;
}
