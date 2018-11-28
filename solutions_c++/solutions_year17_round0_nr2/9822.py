#include <iostream>
#include <string>

using namespace std;

int main()
{
        short T;
        cin>>T;
        int case_number = 1;
        while(case_number <=T)
        {
                unsigned long long int N;
                cin>>N;

                if(N<10)
                {
                        cout<< "Case #" << case_number << ": " << N << "\n";
                }
                else
                {
                        string intStr = to_string(N);
                        unsigned int i = N, size=1;
                        size = intStr.size();
                        i = size - 1;
                        short carry = 0;
                        while(i>0)
                        {
                                intStr[i-1] -= carry;
                                carry = 0;
                                if((intStr[i]<intStr[i-1]) || intStr[i] == '0')
                                {
                                        //cout<<intStr[i]<<"is strictly smaller than"<<intStr[i-1]<<"\n";
                                        intStr[i] = '9';
                                        intStr[i-1] -= 1;
                                        if(intStr[i-1] == -1)
                                        {
                                                intStr[i-1] = '9';
                                                carry = 1;
                                        }
                                }
                                if(i==1 && intStr[0] == '0')
                                {
                                        intStr[0] = '9';
                                        intStr.resize(size-1);
                                }
                                i--;
                        }
                        i = 0;
                        //cout<<"Size of intStr = "<< intStr.size();

                        bool change = 0;
                        while(i < intStr.size())
                        {
                                //bool change = 0;
                                if(intStr[i] == '9')
                                        change = 1;
                                if(change == 1 )
                                        intStr[i] = '9';
                                i++;
                        }
                        cout<< "Case #" << case_number << ": " << intStr <<"\n";
                }
                case_number++;
        }
}
