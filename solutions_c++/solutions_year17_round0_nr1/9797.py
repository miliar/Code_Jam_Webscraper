#include<iostream>
#include<fstream>
#include<stdio.h>
#include<string.h>
using namespace std;


int main()
    {   int noofcases,binaryconvert[25],k,i,j,length,pos=0,w,a;
        int count1=0,count2=0,flag=0,count3=1;
        char string1[30];
        int temp,temp2;
        ifstream fin("test.txt");
        ofstream fout("output.txt");

        while(!fin.eof())
        {
            count2=0;
            flag=0;
            if(count1==0)
            {

                fin>>temp;
                count1=1;
                continue;
            }
            fin>>string1;
            fin>>k;
            cout<<string1<<endl;
            cout<<k<<endl;
            length=strlen(string1);
            for(i=0;i<length;i++)
            {
                if(string1[i]=='+')
                {
                    binaryconvert[i]=1;
                }
                 if(string1[i]=='-')
                {
                    binaryconvert[i]=0;
                }
            }

            for(a=0;a<length;a++)
            {
                if(binaryconvert[a]==0)
                {
                    pos=a;
                    temp2=length-a;
                    if(temp2<k)
                    {
                    flag=1;
                    break;
                    }
                    cout<<endl;
                        for(i=0;i<length;i++)
                        {
                            cout<<binaryconvert[i];
                        }
                    for(j=0;j<k;j++)
                    {
                        if(binaryconvert[pos]==0)
                        {
                            binaryconvert[pos]=1;

                        }
                        else if(binaryconvert[pos]==1)
                        {
                            binaryconvert[pos]=0;
                        }
                        cout<<endl;
                        for(w=0;w<length;w++)
                        {
                            cout<<binaryconvert[w];
                        }
                        pos++;
                        }

                 count2++;
                }
            }
            for(w=0;w<length;w++)
                        {
                            if(binaryconvert[w]==0)
                            {
                                flag=1;
                            }
                        }


            if(flag==0)
            {
                fout<<"Case #"<<count3<<": "<<count2<<endl;
            }
            if(flag==1)
            {
                 fout<<"Case #"<<count3<<": "<<"IMPOSSIBLE"<<endl;
            }
            count3++;
            }






return 0;
}

