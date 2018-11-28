#include <bits/stdc++.h>
#define sf scanf
#define pf printf
#define newl '\n'
#define FAST ios_base::sync_with_stdio(0);
#define Case "Case "<<++kase<<": "
#define CaseH "Case #"<<++kase<<": "
#define GRAY 0
#define WHITE 1
#define BLACK 2
#define imax INT_MAX
#define ll long long
#define max3(a,b,c) max(a,max(b,c))

using namespace std;

int tidy(int num){
    stringstream ss;
    string numString , sortedNum;
    ss << num;
    sortedNum = ss.str();
    numString = sortedNum;
    sort(sortedNum.begin(), sortedNum.end());
    if(numString == sortedNum){
        stringstream ss (sortedNum);
        ss >> num;
        return num;
    }else return tidy(--num);
}

int main(){
   int kase = 0;
   int t;
   cin >> t;
   while(t--){
    int x;
    cin >> x ;
    cout<<CaseH<<tidy(x)<<newl;
   }
    return 0;
}