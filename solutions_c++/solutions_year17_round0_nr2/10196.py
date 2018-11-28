#include <iostream>
#include <fstream>
using namespace std;

int isTidy(int digits, int i);
int main()
{
    fstream inputFile;
    inputFile.open ("B-small-attempt0.in");
    int p=0,number=0,temp=0;
    int tidy=0;
    int testCases=0;
        inputFile>>testCases;

    int check=0;
    int digits=0;
    int* nums=new int[testCases];
    for(int p=0;p<testCases;p++){

    inputFile>>number;

	for(int i=1;i<=number;i++)
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
    }




	nums[p]=tidy;


}
    ofstream output;
    output.open("chutiya.txt");
    for(int j=0;j<testCases;j++)
        output<<"Case #"<<j+1<<": "<<nums[j]<<endl;
    output.close();
}

int isTidy(int i, int digits)
{
    int* array=new int[digits];
    int sent =0;
    int  dig=digits-1;
    int tempVAR=i;
    if(digits<2)
        sent =1;
    else if(digits>1)
    {
        while(tempVAR)
        {
            array[dig]=tempVAR%10;
            tempVAR/=10;
            dig--;
        }
        int q=digits-1;
        for(int p=0;p<q;p++)
        {
            if(array[p]<=array[p+1])
                sent =1;
            else{
                sent =0;
                break;
                }
        }
    }
    return sent ;
}
