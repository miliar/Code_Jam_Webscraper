#include <iostream>
#include <stdio.h>
#include <fstream>
#include <iomanip>

using namespace std;
int t;
long double destin,num,pos[1009],speed[1009];
long double minpost,ti,ans;
ofstream answer;

int main()
{
    answer.open("answer.txt");
    scanf("%d",&t);
    for (int i=0;i<t;i++){
        scanf("%llf%llf",&destin,&num);
        for (int j=0;j<num;j++){
            scanf("%llf%llf",&pos[j],&speed[j]);
            ti=max(ti,(destin-pos[j])/speed[j]);
        }
        ans=destin/ti;
        //cout << std::setprecision(51) << x << "\n";
        answer<<"Case #"<<i+1<<": "<<std::setprecision(20)<<ans<<endl;
        ti=0;
    }
    return 0;
}
