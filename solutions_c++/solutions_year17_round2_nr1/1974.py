#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int t;
    cin>>t;
    for (int x=1;x<t+1;x++){

        double fullDest,num,time=0;
        cin>>fullDest>>num;
        double k,speed;
        for (int i=0;i<num;i++){
            cin>>k>>speed;
            if((fullDest-k)/speed>time)time=(fullDest-k)/speed;
        }
        double z=fullDest/time;
        cout<<"Case #"<<x<<": ";
        std::cout << std::fixed << std::setprecision(6) <<z<<endl;
    }
    return 0;
}
