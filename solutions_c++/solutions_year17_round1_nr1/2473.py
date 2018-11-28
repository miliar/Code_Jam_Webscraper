#include <cstdio>
#include <vector>

int main(int argc, char **argv)
{
    int num_tests;

    scanf(" %d", &num_tests);
    for (int i = 0; i < num_tests; i++)
    {
        int rows, columns;
        scanf(" %d", &rows);
        scanf(" %d", &columns);
        char matrix[25][25];
        bool rows_skipped[25] = {0};
        for (int r = 0; r < rows; r++)
        {
            bool row_is_empty = true;
            for (int c = 0; c < columns; c++)
            {
                scanf(" %c", &matrix[r][c]);
                if (matrix[r][c] != '?') row_is_empty = false;
            }
            if (row_is_empty) rows_skipped[r] = true;
        }

        for (int r = 0; r < rows; r++)
        {
            if (rows_skipped[r]) continue;
            std::vector<int> columns_empty_in_row;
            char current_letter = '?';
            for (int c = 0; c < columns; c++)
            {
                if (matrix[r][c] == '?') 
                {
                    if (current_letter == '?') columns_empty_in_row.push_back(c);
                    else matrix[r][c] = current_letter;
                }
                else
                {
                    current_letter = matrix[r][c];
                    if (!columns_empty_in_row.empty())
                    {
                        for (int k = 0; k < columns_empty_in_row.size(); k++)
                        {
                            matrix[r][columns_empty_in_row[k]] = current_letter;
                        }
                        columns_empty_in_row.clear();
                    }
                }
            }
        }

        int last_non_empty_row = -1;
        int first_non_empty_row = rows - 1;
        for (int r = 0; r < rows; r++)
        {
            if (!rows_skipped[r])
            {
                if (last_non_empty_row == -1)
                {
                    first_non_empty_row = r;
                }
                last_non_empty_row = r;
                continue;
            }

            for (int c = 0; c < columns; c++)
            {
                matrix[r][c] = matrix[last_non_empty_row][c];
            }
        }

        for (int r = 0; r < first_non_empty_row; r++)
        {
            if (!rows_skipped[r]) continue;

            for (int c = 0; c < columns; c++)
            {
                matrix[r][c] = matrix[first_non_empty_row][c];
            }
        }

        printf("Case #%d:\n", i + 1);
        for (int r = 0; r < rows; r++)
        {
            for (int c = 0; c < columns; c++)
            {
                printf("%c", matrix[r][c]);
            }
            printf("\n");
        }
    }

    return 0;
}

