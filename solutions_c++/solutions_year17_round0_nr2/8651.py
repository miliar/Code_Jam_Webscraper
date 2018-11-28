#include<iostream>
#include<fstream>

int main(){
    long long T=0,N=0, ans=0;
    long long n1=0, n2=0;
    std::ifstream iF ("B-small-attempt1.in");
    std::ofstream oF ("output.txt");
    iF>>T;
    for(int j=0;j<T;j++){
        iF>>N;
        for(long long i=1;i<=N;i++){
            n1=0;n2=0;
            int counter=0, counter1=0;
            long long num=i;
            while(num!=0){
                n2=n1;
                n1=num%10;
                num/=10;
                if(counter==0)
                    n2=n1+1;
                if(n2>=n1)
                    counter++;
                counter1++;
            }
            if(counter1==counter)
                ans=i;
        }
        oF<<"Case #"<<j+1<<": "<<ans<<std::endl;
    }
    iF.close();
    oF.close();
    return 0;
}
