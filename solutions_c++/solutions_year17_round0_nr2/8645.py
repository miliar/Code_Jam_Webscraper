#include <iostream>

using namespace std;
#include <vector>

#include <QFile>
#include <QString>
#include <QTextStream>

void tidy_numbers(unsigned long long input, FILE *fp)
{
    int i = 0;
    int n, k, size;
    int first_conflict = 0;
    vector<int> number;
    number.clear();

    while(input != 0)
    {
        number.push_back((int)(input % 10));
        input = input / 10;
    }

    size = number.size();

    for(i = size - 1;i > 0;i--)
    {
        n = number.at(i);
        k = number.at(i - 1);

        if(n > k)
        {
            first_conflict = i;
            number.at(i) = n - 1;
            break;
        }
    }


    for(i = first_conflict;i < size;i++)
    {
        if(i == size - 1)
        {
            first_conflict = size - 1;
            break;
        }

        n = number.at(i);
        k = number.at(i + 1);

        if(n < k)
//        {
//            number.at(i) = 9;
            number.at(i + 1) = k - 1;
//        }
        else
        {
            first_conflict = i;
            break;
        }
    }

    for(i = size - 1;i >= 0;i--)
    {
        if(i >= first_conflict)
        {
            if(number.at(i) != 0)
//                printf("%d", number.at(i));
                fprintf(fp, "%d", number.at(i));
        }
        else
//            printf("9");
            fprintf(fp, "9");
    }

}

int main(int argc, char *argv[])
{
    int cases, i;
    unsigned long long input;
    QFile file("D:\\B-large.in");
    FILE *fp = fopen("D:\\output.txt", "a");

    if(fp && file.open(QIODevice::ReadOnly))
    {
        QTextStream stream(&file);
        while(!stream.atEnd())
        {
            cases = stream.readLine().toInt();
            for(i = 1;i <= cases;i++)
            {
                input = stream.readLine().toLongLong();
    //                printf("Case #%d: ", i);
                fprintf(fp, "Case #%d: ", i);
                tidy_numbers(input, fp);
    //                printf("\n");
                fprintf(fp, "\n");
            }
            fclose(fp);
        }
    }
    file.close();

//    tidy_numbers(input);
//    printf("\n");
    return 0;
}
