#include<iostream>
#include<string>
#include<fstream>
#include<vector>
#include<algorithm>

using namespace std;

class Horse {
    public:
        long long kil;
        int speed;
    
    Horse(long long k, int s)
    {
        kil = k;
        speed = s;
    }


};

int main(){
    fstream outFile("a.out",fstream::out);

    int tests;
    cin>>tests;

    for(int test=1;test<=tests;++test)
    {
        long long d;
        int n;
        cin>>d>>n;
        outFile.precision(8);
        double czas = -1;

        for(int i=0;i<n;++i)
        {
            double tmpD;
            int speed;
            cin>>tmpD>>speed;
            double czas1 = (double)(d-tmpD)/speed;
            if (czas1>czas || czas == -1)
            {
                czas = czas1;
            }
        }

        outFile<<"Case #"<<test<<": "<<fixed<<( (double) d)/czas<<endl;



    }


}