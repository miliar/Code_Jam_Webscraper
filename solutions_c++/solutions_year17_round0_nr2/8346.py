 #include<iostream>
 #include<fstream>

using namespace std;

bool IsTidy(unsigned long long x);

int main()
{   ifstream infile;
    infile.open("B-small-attempt0.in");
    ofstream out("output.txt");
    unsigned long long testCases,num;
    infile>>testCases;
        for(unsigned long long j=1;j<=testCases;j++)
            {
                infile>>num;
                bool flag=false;
                    for(unsigned long long i=num;i>=1;i--)
                    {
                            flag=IsTidy(i);
                                if(flag==true)
                                {
                                out<<"Case #"<<j<<": "<<i<<endl;
                                break;
                                }
}

}
    infile.close();
    out.close();
return 0;
}

bool IsTidy(unsigned long long x)
{
unsigned long long a,b;
while(x!=0)
{
a = x%10;
x/=10;
b = x%10;
if(a<b)
{
return false;
}
}

return true;
}
