#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;

void max_tidy(long long digit[],int &i)
{
    if (i==1)
        return;
for (int q=0;q<i;q++){
    for (int j=i-1;j>=0;j--)
    {
        if (digit[j]>digit[j-1])
            {
                digit[j]-=1;
                int k=j-1;
        while(k>=0)
            {
                digit[k]=9;
                k--;
            }
            }
    }
}
}
int main()
{
    int n;
    ifstream myfile;
    ofstream file;
    file.open("result.txt");
    myfile.open("long_second.txt");
    if (myfile.is_open()){
    myfile>>n;
    for (int j=0;j<n;j++)
        {
    long long num;
    long long arr[20];
    myfile>>num;
    long long temp=num;
    int num_digits=0;
    while (temp!=0)
    {
        arr[num_digits]=temp%10;
        temp/=10;
        num_digits++;
    }

        max_tidy(arr,num_digits);
                {
                    file<<"Case #"<<j+1<<": ";
                    if (arr[num_digits-1]!=0)
                        file<<arr[num_digits-1];
                    for (int k=num_digits-2;k>=0;k--)
                        file<<arr[k];
                    file<<endl;
                }

    }

    return 0;
}
else
    return -1;
}
