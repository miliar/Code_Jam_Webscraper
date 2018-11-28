#include <bits/stdc++.h>
using namespace std;
FILE *fi;
void quickSort(int arr[], int left, int right) {

      int i = left, j = right;

      int tmp;

      int pivot = arr[(left + right) / 2];



      /* partition */

      while (i <= j) {

            while (arr[i] < pivot)

                  i++;

            while (arr[j] > pivot)

                  j--;

            if (i <= j) {

                  tmp = arr[i];

                  arr[i] = arr[j];

                  arr[j] = tmp;

                  i++;

                  j--;

            }

      };



      /* recursion */

      if (left < j)

            quickSort(arr, left, j);

      if (i < right)

            quickSort(arr, i, right);

}
int jat(int g)
{

fi=fopen("ez.txt","at");
 int m,k,sz1=0,sz2=0,u=0;
vector<int>  t(3000000);
for (int i=0;i<3000000;i++) t[i]=0;

scanf("%d%d",&m,&k);t[0]=m;
for ( ;sz1<k;sz1++,sz2+=2)
{

    if (t[sz1]%2==0)
    {
        t[sz2+1]=t[sz1]/2;
        t[sz2+2]=t[sz2+1]-1;


    }
    else
    {
        t[sz2+2]=t[sz2+1]=t[sz1]/2;
    }
    if(sz1!=k-1  && t[sz1]==t[sz1-1])
    {
        u++;
        swap(t[sz2+1],t[sz2+1-u]);
    }
    else u=0;

}
fprintf(fi,"Case #%d: %d %d\n",g+1,t[sz2-1],t[sz2]);
fclose(fi);
  return 0;
}
int main()
{
fi=fopen("ez.txt","wt");
fclose(fi);
int n;
scanf("%d",&n);

for (int i=0;i<n;i++)
{

    jat(i);
}
        return 0;
}
