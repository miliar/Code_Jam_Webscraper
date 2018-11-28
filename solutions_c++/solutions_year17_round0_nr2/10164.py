#include<iostream>
#include<fstream>
#include<stdio.h>
#include<string.h>
#include<conio.h>
using namespace std;


int main()
    {   long long int number,finalnumber,i;
        int j,k,l,m,n,length=0,temp,flag=1,testcase,tempnum,tempdigit;
        int count1=0,count2=1,pos,minnum;
        int intarray[25];
        ifstream fin("test.txt");
        ofstream fout("output.txt");

        while(!fin.eof())
        {

            if(count1==0)
            {
                fin>>testcase;
                count1=1;
                continue;
            }

            fin>>number;
            cout<<number<<endl;

            for(i=0;i<number;i++)
            {
                flag=1;

                finalnumber=number-i;
                cout<<finalnumber<<endl;
                tempnum=finalnumber;
                int lengthCount = 0;
                for(; tempnum != 0; tempnum /= 10, lengthCount++);
                length=lengthCount;
                cout<<length<<endl;
                    pos=length-1;
                    tempnum=finalnumber;
                if(length==1)
                {
                    cout<<"Single Digit";
                }
                else
                {

                for(k=0;k<length;k++)
                {
                    tempdigit=tempnum%10;
                    tempnum=tempnum/10;
                    intarray[pos]=tempdigit;
                    pos--;
                }
                for(n=0;n<length;n++)
                    cout<<intarray[n]<<endl;
                if(length==1)
                {
                    cout<<"Single Digit";
                }


                for(l=0;l<length;l++)
                {
                    for(m=l+1;m<length;m++)
                    {
                        if(intarray[m]<intarray[l])
                        {
                            flag=0;
                            break;
                        }
                    }
                    if(flag==0)
                    {
                        cout<<"BREAKING";
                        break;
                    }
                    else
                    {
                        continue;

                    }
                }

                }

                if(flag==0)
                {
                    continue;
                }
                else
                {
                    fout<<"Case #"<<count2<<": "<<finalnumber<<endl;
                    count2++;
                    break;
                }
                count2++;

            }
        }





      return 0;
    }
