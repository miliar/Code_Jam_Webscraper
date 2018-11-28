#include<bits/stdc++.h>
using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;

    fin.open("prob2.in", ios::in);
    fout.open("output.txt", ios::out);

    int t;
    fin>>t;
    int casecount = 0;
    while(t--)
    {
        casecount++;
        long long int n;
        fin>>n;

        int arr[20];
        for(int i=0; i<20; i++)
            arr[i] = -1;

        int j = 0;
        while(n != 0)
        {
            arr[j] = n%10;
            j++;
            n /= 10;
        }

        for(int i=0; i<(j-1); i++)
        {
            if(arr[i] < arr[i+1])
            {
                for(int k=0; k<=i; k++)
                    arr[k] = 9;
                arr[i+1]--;
            }
        }

        long long int finalans = 0;
        for(int i=j-1; i>=0; i--)
            finalans = finalans*10 + arr[i];

        fout<<"Case #"<<casecount<<": "<<finalans<<endl;
    }

    fin.close();
    fout.close();
}
