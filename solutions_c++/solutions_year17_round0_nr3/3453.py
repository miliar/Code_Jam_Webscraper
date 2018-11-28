#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

ifstream fin("c1.in");
ofstream fout("c1.out");

struct place{
    int num;
    int times;
};

int binsearch(vector<place> ary,int tar,bool &test){
    int left=0;
    int right=ary.size()-1;
    while(left<=right){
        int m=(left+right)/2;
        if(ary[m].num==tar)
            return m;
        else if(ary[m].num<tar)
            left=m+1;
        else
            right=m-1;
    }
    test=false;
    return max(left,right);
}

int main(){
    int t;
    fin>>t;
    for(int l=0;l<t;l++){
        long n,k;
        fin>>n>>k;
        if(n==k){
            fout<<"Case #"<<l+1<<": "<<0<<" "<<0<<endl;
            continue;
        }
        cout<<l+1<<" "<<n<<" "<<k<<endl;
        vector <place> ary;
        place temps;
        temps.num=0;
        temps.times=0;
        ary.push_back(temps);
        temps.num=n;
        temps.times=1;
        ary.push_back(temps);
        for(int i=0;i<k-1;i++){
            int temp=ary.back().num;
            //cout<<ary.size()<<endl;
            ary[ary.size()-1].times--;
            if(ary.back().times==0)
                ary.pop_back();
            temp--;
            int x,y;
            if(temp%2==0){
                x=temp/2;
                y=temp/2;
            }
            else{
                x=temp/2;
                y=temp/2+1;
            }
            bool test=true;
            int pos1=binsearch(ary,x,test);
            if(test){
                ary[pos1].times++;
            }
            else{
                place temp1;
                temp1.num=x;
                temp1.times=1;
                ary.insert(ary.begin()+pos1,temp1);
            }
            test=true;
            int pos2=binsearch(ary,y,test);
            if(test){
                ary[pos2].times++;
            }
            else{
                place temp1;
                temp1.num=y;
                temp1.times=1;
                ary.insert(ary.begin()+pos2,temp1);
            }
        }
        int temp=ary.back().num;
        temp--;
        int x,y;
        if(temp%2==0){
            x=temp/2;
            y=temp/2;
        }
        else{
            x=temp/2;
            y=temp/2+1;
        }
        fout<<"Case #"<<l+1<<": "<<y<<" "<<x<<endl;
    }
}
