//
//  main.cpp
//  b
//
//  Created by   kimtaehoon on 2017. 4. 30..
//  Copyright © 2017년   kimtaehoon. All rights reserved.
//

#include <fstream>
#include <vector>
using namespace std;
bool tmr(pair<pair<int,int>,int> a,pair<pair<int,int>,int> b)
{
    if(a.first.first<b.first.first) return true;
    return false;
}
int main(int argc, const char * argv[]) {
    ifstream in;
    in.open("/Users/kimtaehoon/Desktop/code jam round c/b/b/in.txt");
    ofstream out;
    out.open("/Users/kimtaehoon/Desktop/code jam round c/b/b/out.txt");
    int t;
    in >> t;
    for(int q=1;q<=t;q++)
    {
        vector<pair<int,int> > f,s;
        vector<pair<pair<int,int>,int> > y;
        vector<int> ff,fs,ss;
        int a,b,pp=0,a_sum=0,b_sum=0;
        in >> a >> b;
        for(int e=0;e<a;e++)
        {
            int p,r;
            in >> p >> r;
            if(p>r)
            {
                f.push_back({p,1440});
                y.push_back({{p,1440},1});
                f.push_back({0,r});
                y.push_back({{0,r},1});
                a_sum+=1440-p+r;
            }
            else{
                f.push_back({p,r});
                y.push_back({{p,r},1});
                a_sum+=r-p;
            }
        }
        for(int e=0;e<b;e++)
        {
            int p,r;
            in >> p >> r;
            if(p>r)
            {
                s.push_back({p,1440});
                y.push_back({{p,1440},2});
                s.push_back({0,r});
                y.push_back({{0,r},2});
                b_sum+=1440-p+r;
            }
            else{
                s.push_back({p,r});
                y.push_back({{p,r},2});
                b_sum+=r-p;
            }
        }
        sort(y.begin(),y.end(),tmr);
        for(int e=1;e<y.size();e++)
        {
            int left=y[e-1].first.second;
            int left_num=y[e-1].second;
            int right=y[e].first.first;
            int right_num=y[e].second;
            if(left_num!=right_num)
            {
                fs.push_back(right-left);
            }
            if(left_num==1&&right_num==1)
            {
                ff.push_back(right-left);
            }
            if(left_num==2&&right_num==2)
            {
                ss.push_back(right-left);
            }
        }
        int left=1440-y[y.size()-1].first.second;
        int left_num=y[y.size()-1].second;
        int right=y[0].first.first;
        int right_num=y[0].second;
        if(left_num!=right_num)
        {
            fs.push_back(right+left);
        }
        if(left_num==1&&right_num==1)
        {
            ff.push_back(right+left);
        }
        if(left_num==2&&right_num==2)
        {
            ss.push_back(right+left);
        }
        sort(ff.begin(),ff.end());
        sort(ss.begin(),ss.end());
        sort(fs.begin(),fs.end());
        pp+=fs.size();
        a_sum=720-a_sum;
        b_sum=720-b_sum;
        for(int e=0;e<ff.size();e++)
        {
            if(a_sum>ff[e])
            {
                a_sum-=ff[e];
                ff[e]=0;
            }
            else{
                ff[e]-=a_sum;
                break;
            }
        }
        for(int e=0;e<ss.size();e++)
        {
            if(b_sum>ss[e])
            {
                b_sum-=ss[e];
                ss[e]=0;
            }
            else{
                ss[e]-=b_sum;
                break;
            }
        }
        for(int e=0;e<ff.size();e++)
        {
            if(ff[e]!=0) pp+=2;
        }
        for(int e=0;e<ss.size();e++)
        {
            if(ss[e]!=0) pp+=2;
        }
        out << "Case #"<<q<<": "<<pp<<endl;
    }
    return 0;
}
