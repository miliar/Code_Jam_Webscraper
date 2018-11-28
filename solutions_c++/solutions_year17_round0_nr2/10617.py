#include<iostream>
using namespace std;
#include<fstream>
bool check(double m)
{
    int i=0,r;
    int a[10]={0,0,0,0,0,0,0,0,0,0};
    bool flag;
    while(m>0)
    {
        r = int(m)%10;
        a[i] = r;
        m = int(m)/10;
        i++;
    }

    int j=0;
    while(j<i-1)
    {
        if(a[j]>=a[++j])
            flag = true;
        else
        {
            return false;
        }
    }
    return true;

}
int main()
{
    int t=1,i=1;

    ifstream fin("C:\\Users\\Admin\\Downloads\\B-small-attempt6.in");
    ofstream fout("output.out");
    fin>>t;
    while(t--)
    {
        double n;
        fin >> n;
  //      cin>>n;
        while(true)
        {
            if(check(n)==false)
                n--;
            else
                break;
        }

        fout << "Case #" << i++ << ": " << n<<"\n";
    }
    fin.close();
    fout.close();
    return 0;
}
