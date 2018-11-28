#include <iostream>
#include <fstream>
#include <string>

using namespace std;


string findLastTidy(string num)
{
    string lastTidy=num;
    int size = num.size();
    int i=0;
    while(i<size-1)
    {
        if(i+1 < size && (int)(num[i]) > (int)(num[i+1]))
        {
            int now = (int)num[i] -1;

            if(num[i] != '1' && num[i] != num[i-1])
            {
                num[i] = (char)now;
                for(int j=i+1; j<size; j++, i++)
                {
                    num[j] = '9';
                }
            }
            else
            {
                //cout<<"here";
                for(int j=size-1; j>0; j--, i++)
                {
                    num[j] = '9';
                    //cout<<"checking: "<<num[j]<<" "<<num[j-1]<<endl;
                    if(j-1 ==0 && num[j-1] == '1')
                    {
                        num.erase(num.begin()+0);
                    }
                    else
                    {
                        //cout<<num[j]<<" "<<num[j-1]<<endl;
                        num[j-1] = (char)((int)num[j-1] - 1);
                    }



                }
            }
        }
        //else if(i+1 < size && (int)(num[i]) == 1)

        i++;
    }
    //cout<<endl;
    lastTidy = num;
    return lastTidy;
}

int main()
{
    ifstream infile("B-small-attempt1.in");
    ofstream myfile;
    myfile.open ("B-small-attempt1.out");

    int total;
    infile >> total;
    int caseNo = 0;
    while(++caseNo<=total)
    {
        //string str;
        string lastNum;
        infile >> lastNum;

        string tidyNumber = findLastTidy(lastNum);

        myfile<<"Case #"<<caseNo<<": "<<tidyNumber<<endl;
    }


    return 0;
}
