#include<iostream>
#include<string>
#include<algorithm>
#include<fstream>
#include<vector>
using namespace std;


struct st{
    unsigned long long ls =0;
    unsigned long long rs =0;
    bool occ = false;
    bool minf = false;
    bool maxf = false;
    unsigned long long minint =0;
    unsigned long long maxint =0;
};



void mark(st *arr,int n)
{
    
    for(int i=0;i<n;i++)
    {
        
            if(!arr[i].occ)
            {
                arr[i].ls = 0;
                arr[i].rs = 0;
                arr[i].minf = false;
                arr[i].maxf = false;
            }
        
        if(!arr[i].occ)
        {
            for(int k=i+1;k<n;k++)
            {
                if(!arr[k].occ)
                {
                    arr[i].rs++;
                }
                else
                    break;
            }
            for(int k=i-1;k>=0 && !arr[k].occ;k--)
            {
                if(!arr[k].occ)
                {
                    arr[i].ls++;
                }
                else
                    break;
            }
            
            arr[i].minint = min(arr[i].ls,arr[i].rs);
            arr[i].maxint = max(arr[i].ls,arr[i].rs);
        }
    }
}



int main()
{
    ifstream fin;
    ofstream fout;
    fout.open("c:/Users/hamza/Desktop/codejam/stalls/out.txt");
    fin.open("c:/Users/hamza/Desktop/codejam/stalls/in.txt");
    
    if(!fin.is_open())
    {
        cout<<"File not Found"<<endl;
        return 0;
    }
    
    
    int cases;
    fin>>cases;
    unsigned long long  n = 0;
    unsigned long long  k = 0;
    
    
    
    for(int cc=0;cc<cases;cc++)
    {
        fin>>n;
        fin>>k;
        
        
        
        
        st *arr = new st[n];
        int index = 0;
        unsigned long long max = 0;
        unsigned long long min = 0;
        for(int i=0;i<k;i++)
        {
            max =0;
            min = 0;
            mark(arr,n);
            
            //for(int v =0;v<n;v++)
              //  cout<<arr[v].ls<<" "<<arr[v].rs<<" "<<arr[v].minint<<" "<<arr[v].maxint<<endl;
            
            for(int j=0;j<n;j++)
            {
                if(!arr[j].occ){
                if(max < arr[j].minint)
                    max = arr[j].minint;
                }
                
            }
            for(int j=0;j<n;j++)
            {
                if(!arr[j].occ){
                if(arr[j].minint == max)
                    arr[j].minf = true;
                }
            }
            int count =0;
            bool con = false;
            for(int j=0;j<n;j++)
            {
                if(!arr[j].occ){
                if(arr[j].minf)
                    count++;
                }
                if(count>1)
                {
                    con = true;
                    break;
                }
                    
                
            }
            
            if(con)
            {
                
                for(int j=0;j<n;j++)
                {
                    if(!arr[j].occ){
                    if(arr[j].minf)
                    {
                    if(min < arr[j].maxint)
                        min = arr[j].maxint;
                    }
                    }
                    
                }
                for(int j=0;j<n;j++)
                {
                    if(!arr[j].occ){
                    if(arr[j].minf)
                    {
                    if(arr[j].maxint == min)
                        arr[j].maxf = true;
                    }
                    }
                }
                
                int count1 =0;
                bool con1 = false;
                for(int j=0;j<n;j++)
                {
                    if(!arr[j].occ){
                    if(arr[j].maxf)
                        count1++;
                    }
                    if(count1>1)
                    {
                        con1 = true;
                        break;
                    }
                    
                }
                
                    for(int j=0;j<n;j++)
                    {
                        if(arr[j].minf && arr[j].maxf)
                        {
                            if(!arr[j].occ){
                                if(arr[j].maxint == min)
                            {
                                arr[j].occ = true;
                                index = j;
                                break;
                            }
                            }
                        }
                    }
                    
            }
            
            else
            {
                for(int j=0;j<n;j++)
                {
                    if(!arr[j].occ){
                    if(arr[j].minf)
                    {
                    if(arr[j].minint == max)
                    {
                        arr[j].occ = true;
                        index = j;
                        break;
                    }
                        
                    }
                    }
                }

            }
            
            
        }
        
       fout<<"Case #"<<cc+1<<": "<<arr[index].maxint<<" "<<arr[index].minint<<endl;
        
    }
    
    return 0;
}
