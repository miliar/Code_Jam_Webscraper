    #include<bits/stdc++.h>
    #define q long long int
    using namespace std;
     
    int main()
    {
        q oooo;
        q kkk;
        q k;
        q sora;
        cin>>oooo;
        for(int i=0; i<oooo; i++)
        {
            cin>>kkk;
            cin>>k;
     
            priority_queue<q> prior_queue;
            q left,right,max1,min1;
            sora = kkk;
            for(int j=0; j<k; j++)
            {
               sora = sora -1;
               left = sora/2;
               right = sora - left;
               prior_queue.push(left);
               prior_queue.push(right);
               max1=max(left,right);
               min1=min(left,right);
               sora=prior_queue.top();
               prior_queue.pop();
            }
            cout<<"Case #"<<i+1<<": "<<max1<<" "<<min1<<endl;
            while(!prior_queue.empty())
            {
    			prior_queue.pop();
            }
        }
        return 0;
    }