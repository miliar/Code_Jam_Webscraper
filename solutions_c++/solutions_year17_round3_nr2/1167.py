#include<iostream>
#include<string>
#include<fstream>
#include<vector>
#include<algorithm>
#include<unordered_map>

using namespace std;


int main(){
    fstream outFile("b1.out",fstream::out);

    int tests;
    cin>>tests;

    for(int test=1;test<=tests;++test)
    {
        int ac,aj;
        cin>>ac>>aj;

        vector<int> size;
        int tmp,tmp1;

        vector<pair<int,int>> zajC;
        vector<pair<int,int>> zajJ;

        for(int i=0;i<ac;++i)
        {
            cin>>tmp>>tmp1;
            zajC.push_back(make_pair(tmp,tmp1));
        }

        for(int i=0;i<aj;++i)
        {
            cin>>tmp>>tmp1;
            zajJ.push_back(make_pair(tmp,tmp1));
        }


        if((aj == 1 && ac<2) || (ac == 1 && aj<2))
        {
            outFile<<"Case #"<<test<<": "<<2<<endl;
            continue;
        }
        else if(aj == 2)
        {
            int sta = 0, sto = 0;
            int sta1 = 0, sto1 = 0;
            if (zajJ[0].second>zajJ[1].second)
            {
                sta1 = zajJ[0].first;
                sto1 = zajJ[0].second;
                sta = zajJ[1].first;
                sto = zajJ[1].second;
            }
            else 
            {
                sta1 = zajJ[1].first;
                sto1 = zajJ[1].second;
                sta = zajJ[0].first;
                sto = zajJ[0].second; 
            }

            if((sto1-sta<=720) || (sto+1440-sta1<=720))
            {
                outFile<<"Case #"<<test<<": "<<2<<endl;
            }
            else
            {
                outFile<<"Case #"<<test<<": "<<4<<endl;
            }
        }
        else if(ac == 2)
        {
            int sta = 0, sto = 0;
            int sta1 = 0, sto1 = 0;
            if (zajC[0].second>zajC[1].second)
            {
                sta1 = zajC[0].first;
                sto1 = zajC[0].second;
                sta = zajC[1].first;
                sto = zajC[1].second;
            }
            else 
            {
                sta1 = zajC[1].first;
                sto1 = zajC[1].second;
                sta = zajC[0].first;
                sto = zajC[0].second; 
            }

            if((sto1-sta<=720) || (sto+1440-sta1<=720))
            {
                outFile<<"Case #"<<test<<": "<<2<<endl;
            }
            else
            {
                outFile<<"Case #"<<test<<": "<<4<<endl;
            }
        }
        

    }
}