#include<iostream>
using namespace std;
/*void set(char cake[25][25],int flag[25],int R,int C)
{
	int i,j;
	for(i=0;i<R;i++)	//copy right
		for(j=0;j<C;j++)
			if(cake[i][j]=='?')
				if(cake[i][j+1]!='?' && j+1<C )
					cake[i][j]=cake[i][j+1];
		cout<<endl<<right copy done<<endl;
     for(i=0;i<R;i++)     //PRINT OUTPUT CAKE
                  {       for(j=0;j<C;j++)
		                            cout<<cake[i][j];
					                    cout<<endl;
							                    }
	cout<<endl<<"down copy done"
	  for(i=0;i<R;i++)
	       for(j=0;j<C;j++)
	            if(cake[i][j]=='?')
	                 if(cake[i+1][j]!='?' && j+1<R )
	                        cake[i][j]=cake[i+1][j];

	  for(i=0;i<R;i++)
	        for(j=0;j<C;j++)
	              if(cake[i][j]=='?')
	                   if(cake[i][j+1]!='?' && j-1<C )
	                         cake[i][j]=cake[i][j+1];

}
*/
int main()
{
	int R,C,T=1,d=1;
	int i,j,k;
	cin>>T;
	while(T--)
	{
		cin>>R>>C;
		char cake[25][25];
		int found=0;
		char temp;
		for(i=0;i<R;i++)
			for(j=0;j<C;j++)
				cin>>cake[i][j];

/*		for(i=0;i<R;i++)     //PRINT OUTPUT CAKE
	     {       for(j=0;j<C;j++)
		          cout<<cake[i][j];
		cout<<endl;
		}
*/

		for(i=0;i<R;i++)
		{
			found=0;
			/*if(cake[i][0]!='?')
			{
				temp=cake[i][0];
				found=1;
			}
			*/
			for(j=0;j<C;j++)
			{
				 if(cake[i][j]!='?')
	                        {
                        	        temp=cake[i][j];
                	                found=1;
        	                }

				if(cake[i][j]=='?')
				{
					k=j;
					while(k+1<C)
					{
						k++;
						if(cake[i][k]!='?')
						{
							found=1;
							temp=cake[i][k];
							for(;j<k;j++)
								cake[i][j]=temp;
							break;
						}
						
					}
				}						
			
			}//end j
			if(found)
			{
				for(j=0;j<C;j++)
					if(cake[i][j]=='?')
						cake[i][j]=temp;
			}


		}	//ROW PARSING ENDS
			

		for(i=0;i<C;i++)
                {
                        found=0;
                       /* if(cake[0][i]!='?')
                        {
                                temp=cake[0][i];
                                found=1;
                        }
			*/
                        for(j=0;j<R;j++)
                        {
				 if(cake[j][i]!='?')
        	                {
                	                temp=cake[j][i];
                        	        found=1;
                        	}

                                if(cake[j][i]=='?')
                                {
                                        k=j;
                                        while(k+1<R)
                                        {
                                                k++;
                                                if(cake[k][i]!='?')
                                                {
                                                        found=1;
                                                        temp=cake[k][i];
                                                        for(;j<k;j++)
                                                                cake[j][i]=temp;
                                                        break;
                                                }

                                        }
                                }

                        }//end j
                        if(found)
                        {
                                for(j=0;j<R;j++)
                                        if(cake[j][i]=='?')
                                                cake[j][i]=temp;
                        }
		

		}//end i

	cout<<"Case #"<<d++<<":"<<endl;

     for(i=0;i<R;i++)     //PRINT OUTPUT CAKE
             {       for(j=0;j<C;j++)
                          cout<<cake[i][j];
                cout<<endl;
                }





	}//end T

	
}
