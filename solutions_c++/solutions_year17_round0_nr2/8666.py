#include <iostream>
#include <fstream>

using namespace std;

int isTidy(int digits, int i);
int main()
{
    fstream file;
    file.open ("B-small-attempt2.in");
    int p=0;
    int num=0;
    int temp=0;
    int tidy=0;
    int tT=0;
    do
    {
        file>>tT;
    }while(tT>100 || tT<1);
    int check=0;
    int digits=0;
    int* arr=new int[tT];
    for(int p=0;p<tT;p++){
    do{
    file>>num;
    }while(num<1 || num>1000);
    for(int i=1;i<=num;i++)
    {
        temp=i;
        while(temp>0)
        {
            temp/=10;
            digits++;
        }
    check=isTidy(i, digits);
    digits=0;
    if (check==1)
        tidy=i;
    }                        //check=IsTidy(i, digits);
    //reset


    //
    arr[p]=tidy;


}
    ofstream output;
    output.open("new.txt");
    for(int j=0;j<tT;j++)
        output<<"Case #"<<j+1<<": "<<arr[j]<<endl;
    output.close();
}

int isTidy(int i, int digits)
{
    int* array=new int[digits];
    int flag=0;
    int  dig=digits-1;
    int copy=i;
    if(digits<2)
        flag=1;
    else if(digits>1)
    {
        while(copy)
        {
            array[dig]=copy%10;
            copy/=10;
            dig--;
        }
        int q=digits-1;
        for(int p=0;p<q;p++)
        {
            if(array[p]<=array[p+1])
                flag=1;
            else{
                flag=0;
                break;
                }
        }
    }
    return flag;
}


